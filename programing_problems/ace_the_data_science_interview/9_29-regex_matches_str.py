"""
Ace The Data Science Interview

Hard Problems
9.29. Two Sigma: Given an input string and a regex, write a function that checks whether  the regex
matches the input string.  The input string is composed of the lowercase letters a-z. The regular
expression contains lowercase a-z, '?' or '*', where the '?' matches any one character, and the '*'
matches any arbitrary number of characters (empty as well). For example, if the input string
is "abcdba" and the regex is "a*c?*", return true. However, if the regex was instead "b*c?*"
return false.
"""
# s is string, p is the regex
def is_match(s: str, p: str) -> bool:

    def dfs(i, j):
        if i >= len(s) or j >= len(p):
            return True
        if j >= len(p):
            return False

        match = i < len(s) and (s[i] == p[j] or p[j] == '.')
        if (j+1 < len(p)) and p[j+1] == '*':
            return (dfs(i, j+2) or  # don't use star
                (match and dfs(i+1, j)))  # use star and the existing char matches

        if match:
            return dfs(i+1, j+1)

        return False

    return dfs(0, 0)


if __name__ == "__main__":
    s = 'aa'
    p = 'a'
    expected_value = False

    actual_value = is_match(s, s)
    print("Test 1:", actual_value == expected_value,
        "actual:", actual_value,
        "expected:", expected_value
    )

    s = 'aa'
    p = 'a*'
    expected_value = True

    actual_value = is_match(s, s)
    print("Test 2:", actual_value == expected_value,
        "actual:", actual_value,
        "expected:", expected_value
    )

    s = 'ab'
    p = '.*'
    expected_value = True

    actual_value = is_match(s, s)
    print("Test 3:", actual_value == expected_value,
        "actual:", actual_value,
        "expected:", expected_value
    )
