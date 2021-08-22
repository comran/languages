import numpy as np
from mlxtend.data import loadlocal_mnist
import matplotlib.pyplot as plt
import os
import random
from threadpoolctl import threadpool_limits


def vectorized_result(j):
    x = np.zeros((10, 1))
    x[j] = 1.0
    return x

def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-z))

def sigmoid_prime(z):
    return sigmoid(z) * (1 - sigmoid(z))

def cost_derivative(output_activations, y):
    return output_activations - y

class Network:
    def __init__(self, sizes):
        self.num_layers = len(sizes)
        self.sizes = sizes
        self.biases = [np.random.randn(y, 1) for y in sizes[1:]]
        self.weights = [np.random.randn(y, x) for x, y in zip(sizes[:-1], sizes[1:])]

    def feedforward(self, a):
        for b, w in zip(self.biases, self.weights):
            a = sigmoid(np.dot(w, a) + b)

        return a

    def SGD(self, training_data, epochs, mini_batch_size, eta, test_data=None):
        if test_data:
            n_test = len(test_data)

        n = len(training_data)
        for j in range(epochs):
            random.shuffle(training_data)
            mini_batches = [
                training_data[k:k+mini_batch_size] for k in range(0, n, mini_batch_size)
            ]

            for mini_batch in mini_batches:
                self.update_mini_batch(mini_batch, eta)

            if test_data:
                correct = self.evaluate(test_data)
                print(f"Epoch {j}: {correct} / {n_test} ({correct / n_test * 100.:.2f}%)")

            else:
                print(f"Epoch {j} complete")

    def update_mini_batch(self, mini_batch, eta):
        nabla_b = [np.zeros(b.shape) for b in self.biases]
        nabla_w = [np.zeros(w.shape) for w in self.weights]

        for x, y in mini_batch:
            delta_nabla_b, delta_nabla_w = self.backprop(x, y)
            nabla_b = [nb + dnb for nb, dnb in zip(nabla_b, delta_nabla_b)]
            nabla_w = [nw + dnw for nw, dnw in zip(nabla_w, delta_nabla_w)]

        self.weights = [w - (eta / len(mini_batch)) * nw for w, nw in zip(self.weights, nabla_w)]
        self.biases = [b - (eta / len(mini_batch)) * nb for b, nb in zip(self.biases, nabla_b)]

    def backprop(self, x, y):
        nabla_b = [np.zeros(b.shape) for b in self.biases]
        nabla_w = [np.zeros(w.shape) for w in self.weights]

        activation = x
        activations = [x]
        zs = []
        for b, w in zip(self.biases, self.weights):
            z = np.dot(w, activation) + b
            zs.append(z)
            activation = sigmoid(z)
            activations.append(activation)

        delta = cost_derivative(activations[-1], y) * sigmoid_prime(zs[-1])
        nabla_b[-1] = delta
        nabla_w[-1] = np.dot(delta, activations[-2].T)

        for l in range(2, self.num_layers):
            z = zs[-l]
            sp = sigmoid_prime(z)
            delta = np.dot(self.weights[-l+1].T, delta) * sp
            nabla_b[-l] = delta
            nabla_w[-l] = np.dot(delta, activations[-l-1].T)

        return nabla_b, nabla_w

    def evaluate(self, test_data):
        test_results = [(np.argmax(self.feedforward(x)), y) for x, y in test_data]
        return sum(int(x == y) for x, y in test_results)


data_directory = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data"
)

# From http://yann.lecun.com/exdb/mnist/
train_images_path = os.path.join(data_directory, "train-images-idx3-ubyte")
train_labels_path = os.path.join(data_directory, "train-labels-idx1-ubyte")
test_images_path = os.path.join(data_directory, "t10k-images-idx3-ubyte")
test_labels_path = os.path.join(data_directory, "t10k-labels-idx1-ubyte")

train_X, train_y = loadlocal_mnist(
    images_path=train_images_path,
    labels_path=train_labels_path
)

test_X, test_y = loadlocal_mnist(
    images_path=test_images_path,
    labels_path=test_labels_path
)

train_X = [np.reshape(x, (784, 1)).astype(float) for x in train_X]
train_y_one_hot = [vectorized_result(x) for x in train_y]
test_X = [np.reshape(x, (784, 1)).astype(float) for x in test_X]


training_data = [(data.astype(float) / 256., category) for data, category in zip(train_X, train_y_one_hot)]
test_data = [(data / 256., category) for data, category in zip(test_X, test_y)]

net = Network([784, 30, 10])

with threadpool_limits(limits=4, user_api="blas"):
    net.SGD(training_data, 30, 10, 3.0, test_data=test_data)
