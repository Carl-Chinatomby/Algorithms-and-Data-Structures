"""
Ace The Data Science Interview


Hard Problems
9.25. Citadel: Given a string with left and right parenthesis, write a function to determine the length
of the longest well-formed substring. For example, if the input string is ")(())(", then return 4,
since the longest well-formed string is "(())".
"""
# def length_of_longest_well_formed_paren(string):
#     count = 0
#     stack = []
#     for c in string:
#         if c == ')' and stack:
#             left = stack.pop()
#             count += 2
#         elif c == '(':
#             stack.append(c)
#     return count

def length_of_longest_well_formed_paren(string):
    stack = [-1] # initialized for the case where the string starts with a ) which will be discarded
    longest = 0
    for i in range(len(string)):
        if string[i] == '(':
            stack.append(i)
        else:
            stack.pop()
            if len(stack) == 0: # There should be one if it's a match because we added a extra dummy val
                stack.append(i) # This is the start of the str now
            else:
                longest = max(longest, i - stack[-1]) # length, current - start
    return longest


if __name__ == "__main__":
    string = ")(())("
    expected_value = 4

    actual_value = length_of_longest_well_formed_paren(string)
    print("Test 1:", actual_value == expected_value,
        "actual:", actual_value,
        "expected:", expected_value
    )
