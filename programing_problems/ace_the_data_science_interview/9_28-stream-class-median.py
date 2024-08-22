"""
Ace The Data Science Interview

Hard Problems
9.28. Citadel: Given an continuous stream of integers, write a class with functions to add new integers
to the stream, and a function to calculate the median at any time.
"""
import heapq


class IntegerStream:
    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        heapq.heapify(self.min_heap)
        heapq.heapify(self.max_heap)

    def add_num(self, num):
        if not self.min_heap:
            heapq.heappush(self.min_heap, num)
        elif not self.max_heap:
            heapq.heappush(self.max_heap, -1 * num)
        elif num < self.max_heap[0]:
            heapq.heappush(self.max_heap, -1 * num)
        else:
            heapq.heappush(self.min_heap, num)

        # Balance step
        if len(self.max_heap) - len(self.min_heap) > 1:
            top = heapq.heappop(self.max_heap) * -1
            heapq.heappush(self.min_heap, top)
        elif len(self.min_heap) - len(self.max_heap) > 1:
            top = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -1 * top)

    def get_median(self):
        if len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0]
        elif len(self.min_heap) < len(self.max_heap):
            return selp.max_heap[0]
        else:
            print(self.min_heap[0], self.max_heap[0])
            return (self.min_heap[0] + -1 * self.max_heap[0]) / 2


if __name__ == "__main__":
    intstream = IntegerStream()
    intstream.add_num(1)
    intstream.add_num(2)
    intstream.add_num(3)
    intstream.add_num(4)
    expected_value = 2.5

    actual_value = intstream.get_median()
    print("Test 1:", actual_value == expected_value,
        "actual:", actual_value,
        "expected:", expected_value
    )

    intstream.add_num(5)
    expected_value = 3
    actual_value = intstream.get_median()
    print("Test 2:", actual_value == expected_value,
        "actual:", actual_value,
        "expected:", expected_value
    )
