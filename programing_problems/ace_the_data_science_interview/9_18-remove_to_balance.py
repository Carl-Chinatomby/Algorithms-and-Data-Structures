"""
Ace The Data Science Interview


Medium Problems
9.18. Palantir: Given a string with lowercase letters and left and right parenthesis, remove the
minimum number of parenthesis so that the string is valid (every left parenthesis is correctly
matched by a corresponding right parenthesis). For example, if the  string is ")a(b((cd)e(f)g)"
then return is "ab((cd)e(f)g)"
"""
from collections import deque

def remove_unnecessary_paren(string):
    q = deque()
    for c in string:
        if not c.isalpha():
            if q and c == ')' and q[-1] == '(':
                q.pop()
            else:
                q.append(c)


    output = ""
    for c in string:
        if q and c == q[0]:
            q.popleft()
        else:
            output += c

    return output


if __name__ == "__main__":
    string = ")a(b((cd)e(f)g)"
    expected_value = "ab((cd)e(f)g)"

    actual_value = remove_unnecessary_paren(string)
    print("Test 1:", actual_value == expected_value,
        "actual:", actual_value,
        "expected:", expected_value
    )
