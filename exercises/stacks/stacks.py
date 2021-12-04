#!/usr/bin/env python3
"""
`stacks` implementation and driver

@authors:
"""

import pathlib

from typing import Union

from pythonds3.basic import Stack


class StackError(Exception):
    """Stack errors"""

    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)


class TokenError(Exception):
    """Token errors"""

    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)


def rev_string(my_str: str) -> str:
    """Reverse characters in a string using a stack"""
    # TODO: Implement this function
    my_stack = Stack()
    reverse = ''
    for a in my_str:
        my_stack.push(a)
    for b in range(len(my_str)):
        reverse += my_stack.pop()
    return reverse
    ...


def par_checker(line: str) -> bool:
    """Textbook implementation"""
    stack = Stack()
    balanced = True
    i = 0
    while i < len(line) and balanced:
        symbol = line[i]
        if symbol == "(":
            stack.push(symbol)
        else:
            if stack.is_empty():
                balanced = False
            else:
                stack.pop()
        i = i + 1
    return balanced and stack.is_empty()


def par_checker_ext(line: str) -> bool:
    """Check if parentheses are balanced"""
    # TODO: Implement this function
    parStack = Stack()
    brktStack = Stack()
    curlStack = Stack()
    angStack = Stack()
    balanced = True
    i = 0
    while i < len(line) and balanced:
        symbol = line[i]
        if symbol == '(':
            parStack.push(symbol)
        elif symbol == '[':
            brktStack.push(symbol)
        elif symbol == '{':
            curlStack.push(symbol)
        elif symbol == '<':
            angStack.push(symbol)
        elif symbol == ")":
            try:
                parStack.pop()
            except:
                balanced = False
        elif symbol == "]":
            try:
                brktStack.pop()
            except:
                balanced = False
        elif symbol == "}":
            try:
                curlStack.pop()
            except:
                balanced = False
        elif symbol == ">":
            try:
                angStack.pop()
            except:
                balanced = False
        i += 1
    if parStack.is_empty() == False or brktStack.is_empty() == False or curlStack.is_empty() == False or angStack.is_empty == False:
        balanced = False
    return balanced
    ...


def par_checker_file(filename: str) -> None:
    """Check expressions in the file"""
    # TODO: Implement this function
    f = open(filename,'r')
    lines = f.read().splitlines()
    for line in lines:
        if par_checker(line):
            print(f'{line} is balanced')
        else:
            print(f'{line} is NOT balanced')
    f.close()
    ...


def base_converter(dec_num: int, base: int) -> str:
    """Convert a decimal number to any base"""
    # TODO: Implement this function
    if base != 2 and base != 8 and base != 16:
        raise ValueError(f"Cannot convert to base {base}.")

    rem_stack = Stack()
    digits = '0123456789ABCDEF'
    while dec_num > 0:
        rem = dec_num % base
        rem_stack.push(digits[rem])
        dec_num = dec_num//base

    num_string = ''
    while not rem_stack.is_empty():
        num_string += rem_stack.pop()
    return num_string
    ...


def rpn_calc(postfix_expr: str) -> Union[int, float]:
    """Evaluate a postfix expression"""
    # TODO: Implement this function
    operand_stack = Stack()
    token_list = postfix_expr.split()
    operators = ['+','-','*','/']
    for token in token_list:
        try:
            token = int(token)
        except:
            pass
        if isinstance(token,int):
            operand_stack.push(int(token))
        else:
            if token not in operators:
                    raise TokenError(f'Unknown token: {token}')
            try:
                operand2 = operand_stack.pop()
                operand1 = operand_stack.pop()
                result = do_math(token,operand1,operand2)
                operand_stack.push(result)
            except:
                raise StackError('Stack is empty')
    answer = operand_stack.pop()
    if not operand_stack.is_empty():
        raise StackError('Stack is not empty')
    return answer
    ...


def do_math(operation: str, operand1: Union[int, float], operand2: Union[int, float]):
    """Evaluate a mathematical operation"""
    # TODO: Implement this function
    if operation == "*":
        return operand1 * operand2
    elif operation == "/":
        return operand1 / operand2
    elif operation == "+":
        return operand1 + operand2
    elif operation == "-":
        return operand1 - operand2
    ...


def main():
    """Main function"""
    print("Reversing a string")
    s = "Hello world"
    print(f"Original: {s}")
    print(f"Reversed: {rev_string(s)}")

    print("Checking parentheses")
    exp = "()({}{[][]<>}{[]})"
    if par_checker(exp):
        print(f"Simple checker says: {exp} is balanced")
    else:
        print(f"Simple checker says: {exp} is not balanced")
    if par_checker_ext(exp):
        print(f"Extended checker says: {exp} is balanced")
    else:
        print(f"Extended checker says: {exp} is not balanced")
    print("Checking a file using the simple checker")
    filename = "parentheses_simple.txt"
    if not pathlib.Path(f"{filename}").exists():
        filename = f"exercises/stacks/{filename}"
    par_checker_file(filename)
    print("Base converter")
    n = 160
    print(f"{n} in binary is {base_converter(n, 2)}")
    print(f"{n} in octal is {base_converter(n, 8)}")
    print(f"{n} in hexadecimal is {base_converter(n, 16)}")
    bases = [0, 1, 3, 42]
    for b in bases:
        try:
            print(f"{n} in base {b} is {base_converter(n, b)}")
        except ValueError as ve:
            print(ve)
    print("RPN Calculator")
    expressions = [
        "2 3 +",
        "2 3 -",
        "3 2 -",
        "2 3 *",
        "3 2 /",
        "1 2 + 3 - 4 5 + / 16 +",
    ]
    for e in expressions:
        print(f"{e} = {rpn_calc(e)}")


if __name__ == "__main__":
    main()
