#!/usr/bin/env python3
"""
https://leetcode.com/problems/backspace-string-compare/
"""
import itertools

def _reversed_striped_char(input):
    skip = 0
    for c in reversed(input): # reversed returns iterator O(n)
        if c == '#':
            skip += 1
        elif skip:
            skip -= 1
        else:
            yield c



def backspace_compare(s: str, t: str) -> bool:
    # O(len(x)+len(t)) time, O(1) space
    if s == t:
        return True

    for x, y in itertools.zip_longest(_reversed_striped_char(s), _reversed_striped_char(t)): # also an interator
        if x != y:
            return False

    return True



def main():
    assert backspace_compare('ab#c', 'ad#c') == True
    assert backspace_compare('ab##', 'c#d#') == True
    assert backspace_compare('a##c', '#a#c') == True
    assert backspace_compare('a#c', 'b') == False

if __name__ == "__main__":
    main()
