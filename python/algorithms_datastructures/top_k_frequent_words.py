# LC 692

import heapq
from typing import List


def topKFrequent(words: List[str], k: int) -> List[str]:
    word_frequencies = {}

    for word in words:
        if word not in word_frequencies:
            word_frequencies[word] = 0

        word_frequencies[word] += 1

    frequency_words = {}
    for word, frequency in word_frequencies.items():
        if frequency not in frequency_words:
            frequency_words[frequency] = []

        frequency_words[frequency].append(word)

    for key in frequency_words.keys():
        heapq.heapify(frequency_words[key])

    heap = list([-x for x in word_frequencies.values()])
    heapq.heapify(heap)

    top_k_frequent = []
    for _ in range(k):
        frequency = heapq.heappop(heap)
        top_k_frequent.append(heapq.heappop(frequency_words[-frequency]))

    return top_k_frequent


################################################################################
# Test cases.
tst = ["this", "is", "is", "a", "this", "test"]
assert topKFrequent(tst, 3) == ["is", "this", "a"]
