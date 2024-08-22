"""
Ace The Data Science Interview


Easy Problems
9.1. Amazon: Given two arrays, write a function to get the intersection of the two. For example,
if A = [1, 2, 3, 4, 5], and B = [0, 1, 3, 7] then you should return [1, 3]
"""

def get_intersection(a, b):
    return list(set(a) & set(b))


if __name__ == "__main__":
    a = [1, 2, 3, 4, 5]
    b = [0, 1, 3, 7]

    actual = get_intersection(a, b)
    expected = [1, 3]
    print("Test 1: ", actual == expected)
