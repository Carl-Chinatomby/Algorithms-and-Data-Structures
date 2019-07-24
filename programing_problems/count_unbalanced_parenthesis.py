#!/usr/bin/env python3
"""
Problem:
Given a list of parenthesis, count the number of unbalanced
parenthesis.
"""


def get_unbalanced_count(parenthesis):
    """return the number of unbalanced parenthesis
    in parenthesis

    :param :parenthesis list/tuple  List of 1 characer parenthesis
    :returns int Number of unbalanced parenthesis
    """
    count = 0
    stack = []
    for val in parenthesis:
        val = val.strip()
        if val.strip() == '(':
            stack.append(val)
        elif val.strip() == ')' and len(stack) > 0:
            stack.pop()
        else:
            count += 1

    return count + len(stack)
