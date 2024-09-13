#!/usr/bin/env python3
import re

def add(left, right):
    return left + right

def subtract(left, right):
    return left - right

def multiply(left, right):
    return left * right

def divide(left, right):
    return left / right

def intdivide(left, right):
    return left // right

def modulus(left, right):
    return left % right

def power(left, right):
    return left ** right


ORDER_OF_OPERATIONS_DICT = {
    '-': subtract,
    '+': add,
    '//': intdivide,
    '%': modulus,
    '/': divide,
    '*': multiply,
    '^': power,
}


def validate_parenthesis(expression):
    left_paren_found = False
    paren_stack = []
    for char in expression:
        try:
            float(char)
        except ValueError:
            if char == '(':
                paren_stack.append(char)
            elif char == ')' and paren_stack:
                paren_stack.pop()
            elif char == ')' and not paren_stack:
                raise ValueError('mismatched parenthesis')
            elif char == ' ':
                continue
            elif char == '.':
                pass  # we do a separate validation for decimals
            elif not ORDER_OF_OPERATIONS_DICT.get(char):
                raise ValueError('Not a valid expression')
            else:
                continue

    if paren_stack:
        raise ValueError('mismatched parenthesis')


def validate_decimals(expression):
    for idx, val in enumerate(expression):
        if val == '.':
            if idx+1 >= len(expression):
                raise ValueError('Not a valid expression')

            try:
                int(expression[idx+1])  # All decimals must be followed by an int
            except:
                raise ValueError('Not a valid expression')


def validate_expression(expression):
    validate_parenthesis(expression)
    validate_decimals(expression)


# def calculate(expression):
#     try:
#         return float(expression) if float(expression) != int(expression) else int(expression) # maybe this should be decimal
#     except ValueError:
#         pass # still an expression

#     for operator, op_fct in ORDER_OF_OPERATIONS_DICT.items():
#         left, op, right = expression.partition(operator)
#         if op:
#             return op_fct(calculate(left), calculate(right))


def calculate_tokens(tokens):
    if len(tokens) == 1:
        result = float(tokens[0])
        return result if not result.is_integer() else int(result)

    for operator, op_fct in ORDER_OF_OPERATIONS_DICT.items():
        op_idx = -1
        try:
            op_idx = tokens.index(operator)
        except ValueError:
            continue

        left, right = tokens[:op_idx], tokens[op_idx+1:]
        return op_fct(calculate_tokens(left), calculate_tokens(right))

# def flatten_expression(expression):
#     try:
#         start = expression.rindex('(') + 1
#     except ValueError: # no more parenthesis
#         return expression

#     end = start + expression[start:].index(')')
#     result = calculate(expression[start:end])
#     expression = expression[:start-1] + str(result) + expression[end+1:]
#     return flatten_expression(expression)


def flatten_token_list(tokens):
    start = None
    for idx in range(len(tokens)-1, -1, -1):
        if tokens[idx] == '(':
            start = idx + 1
            break

    if start is None:
        return tokens

    end = start + tokens[start:].index(')')
    result = calculate_tokens(tokens[start:end])
    tokens = tokens[:start-1] + [result] + tokens[end+1:]
    return flatten_token_list(tokens)


def main():
    print("Welcome to Carl's Cool Calculator. Let's do some Math!")
    #expression = input("Enter in an expression to calculate: ")
    expression = "((3.2+1)*(3*2)+3*(2+(3*3) + 3))"
    validate_expression(expression)

    #expression = flatten_expression(expression)
    #result = calculate(expression)
    tokens = re.findall(r"[(|)|+|-|/|*]|[0-9]*\.*[0-9]+", expression)
    tokens = flatten_token_list(tokens)
    result = calculate_tokens(tokens)

    print("The result is: {}".format(result))


if __name__ == "__main__":
    main()
