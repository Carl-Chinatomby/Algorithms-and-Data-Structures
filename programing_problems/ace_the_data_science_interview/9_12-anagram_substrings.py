"""
Ace The Data Science Interview


Medium Problems
9.12. LinkedIn: Given two strings A and B, write a function to return a list of all the start indices
within A where the substring of A is an anagram of B. For example, if A = "abcdcbac" and
B = "abc", then you want to return [0, 4, 5] since those are the starting indices of substrings of
A that are anagrams of B.
"""
def anagram_substrings(a, b):
    indexes = []
    sorted_b = sorted(b)
    for i in range(0, len(a) -  len(b) + 1): # check windows of b into a
        # The book as a more optimized version by storing character counts and comparing instead of sorting
        if sorted(a[i:i+len(b)]) ==  sorted_b:
            indexes.append(i)
    return indexes



if __name__ == "__main__":
    A = "abcdcbac"
    B = "abc"
    expected_value = [0, 4, 5]

    actual_value = anagram_substrings(A, B)
    print("Test 1: ", actual_value == expected_value,
        "actual: ", actual_value,
        "expected: ", expected_value
    )
