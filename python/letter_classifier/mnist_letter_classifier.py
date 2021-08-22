import numpy as np
from mlxtend.data import loadlocal_mnist
import matplotlib.pyplot as plt
import os

data_directory = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data"
)

train_images_path = os.path.join(data_directory, "train-images-idx3-ubyte")
labels_path = os.path.join(data_directory, "train-labels-idx1-ubyte")

X, y = loadlocal_mnist(
    images_path=train_images_path,
    labels_path=labels_path
)

all_letters = np.unique(y)
all_bincounts = np.bincount(y)
letters_to_bincounts = {k: v for k, v in zip(all_letters, all_bincounts)}
print(letters_to_bincounts)

for image, label in zip(X, y):
    reshaped_image = (np.array(image, dtype="float")).reshape(28,28)
    plt.imshow(reshaped_image, cmap='gray')
    plt.show()
