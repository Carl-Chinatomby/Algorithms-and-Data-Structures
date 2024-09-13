"""
Ace The Data Science Interview


Medium Problems
9.14. Goldman Sachs: Given an array of strings, return a list of lists where each list contains the
strings that are anagrams of one another. For example, if the input is ["abc", "abd", "cab",
"bad", "bca", "acd"] then return: [["abc", "cab", "bca"], ["abd", "bad", "acd"]].
"""
from collections import defaultdict

def anagram_lists(lst):
    anagrams =  defaultdict(list)
    for string in lst:
        anagrams[''.join(sorted(string))].append(string)
    return [val for _, val in anagrams.items()]

if __name__ == "__main__":
    lst = ["abc", "abd", "cab", "bad", "bca", "acd"]
    expected_value = [["abc", "cab", "bca"], ["abd", "bad"], ["acd"]]

    actual_value = anagram_lists(lst)
    print("Test 1: ", actual_value == expected_value)
