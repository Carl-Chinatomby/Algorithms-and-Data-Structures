#!/usr/bin/env python3
"""
Problem:
Find the longest substring with k unique characters in a given string
Given a string you need to print longest possible substring that has exactly M unique characters. If there are more than one substring of longest possible length, then print any one of them.

Examples:

"aabbcc", k = 1
Max substring can be any one from {"aa" , "bb" , "cc"}.

"aabbcc", k = 2
Max substring can be any one from {"aabb" , "bbcc"}.

"aabbcc", k = 3
There are substrings with exactly 3 unique characters
{"aabbcc" , "abbcc" , "aabbc" , "abbc" }
Max is "aabbcc" with length 6.

"aaabbb", k = 3
There are only two unique characters, thus show error message.

Source: Google Interview Question.
"""
from collections import defaultdict

def max_substring(st, k):
    start = 0
    end = 0

    count = defaultdict(int)
    count[st[0]] += 1

    window_size = 1
    window_start = 0

    for i in range(1, len(st)):
        #import pdb; pdb.set_trace()
        count[st[i]] += 1
        end += 1

        # we exceed max unique characters; remove 1 char from left side of window
        while len(count.keys()) > k:
            count[st[start]] -= 1

            # delete key if this character does not exist anymore
            if not count[st[start]]:
                del count[st[start]]

            start += 1

        if end - start + 1 > window_size:
            window_size = end - start + 1
            window_start = start

    return st[window_start:window_start + window_size]


def main():
    s = "aabacbebebe"
    k = 3
    result = max_substring(s, k)
    print(result, len(result))

if __name__ == "__main__":
    main()
