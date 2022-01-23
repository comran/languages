import heapq


class MaxHeapHeapq:
    # Simple maxheap implementation that uses the heapq library, which
    # itself implements minheap.
    #
    # Note that initializing the heap ("heapify") is asymptotically faster than
    # pushing each individual item in a list to the heap.
    def __init__(self, items):
        # Inversion runs in O(n) time.
        self.heap = [-x for x in items]

        # Heapify runs in O(n) time.
        heapq.heapify(self.heap)

    def push(self, item):
        # Pushing to heap takes O(log n) time.
        heapq.heappush(self.heap, -item)

    def pop(self):
        # Popping from heap takes O(log n) time.
        return -heapq.heappop(self.heap)


################################################################################
# Test cases.

tst = list(range(10)) + list(range(10))[::-1]
tst_sorted = sorted(tst, reverse=True)

x = MaxHeapHeapq(tst)
x.push(21)
assert x.pop() == 21

for expected in tst_sorted:
    actual = x.pop()
    assert actual == expected
