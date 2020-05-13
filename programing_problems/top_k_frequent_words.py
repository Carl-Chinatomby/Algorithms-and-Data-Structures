#!/usr/bin/env python3
"""
Given a book of words. Assume you have enough main memory to accommodate all words. design a data structure to find
top K maximum occurring words. The data structure should be dynamic so that new words can be added.
"""
from collections import defaultdict
from heapq import (
    heapify,
    heappush,
    heappop,
    heapreplace,
    heappushpop,
)


def get_top_k_freq(input_str, k):
    words = input_str.split()
    word_cnt = defaultdict(int)
    for word in words:
        word_cnt[word.lower()] += 1

    min_heap = []
    heapify(min_heap)
    # loop through the hash and add values to the heap, until size of heap > k
    num_of_words = 0
    for word, cnt in word_cnt.items():
        # once size of heap is =k, we're doing a  pushpop if the root of heap is < current value
        if num_of_words < k:
            heappush(min_heap, (cnt, word))
            num_of_words += 1
        elif min_heap[0][0] < cnt:
            heappushpop(min_heap, (cnt, word))

    # return the heap, various sorting options or manips can be done here
    return min_heap
    #return sorted(min_heap, key=lambda x: (-1*x[0], x[1]))



def main():
    input_str = """
    Welcome to the world of Geeks
    This portal has been created to provide well written well thought and well explained
    solutions for selected questions If you like Geeks for Geeks and would like to contribute
    here is your chance You can write article and mail your article to contribute at
    geeksforgeeks org See your article appearing on the Geeks for Geeks main page and help
    thousands of other Geeks
    """
    assert get_top_k_freq(input_str, 5) == {
        'your': 3,
        'well': 3,
        'and': 4,
        'to': 4,
        'Geeks': 6,
    }


if __name__ == "__main__":
    main()
