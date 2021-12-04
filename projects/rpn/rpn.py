#!/usr/bin/env python3
"""
`rpn` implementation and driver

@authors: Roman Yasinovskyy
@version: 2021.9
"""

from pythonds3.basic import Stack


class StackError(Exception):
    """Stack errors"""

    def __init__(self, *args, **kwargs):
        """Initializer"""
        Exception.__init__(self, *args, **kwargs)


class TokenError(Exception):
    """Token errors"""

    def __init__(self, *args, **kwargs):
        """Initializer"""
        Exception.__init__(self, *args, **kwargs)


def postfix_eval(postfix_expr: str) -> float:
    """Evaluate a postfix expression

    :param postfix_expr: an expression (line) to evaluate
    :return: floating-point result of the evaluation
    >>> postfix_eval("1 2 +")
    3
    >>> postfix_eval("1 2 -")
    -1
    >>> postfix_eval("2 3 *")
    6
    >>> postfix_eval("1 2 /")
    0.5
    >>> postfix_eval("1 2 //")
    0
    >>> postfix_eval("2 3 **")
    8
    """
    # TODO: Implement this function
    operand_stack = Stack()
    token_list = postfix_expr.split()
    token_list.pop()
    operators = ['+','-','*','/','//','**','%']
    if len(token_list) == 0:
        raise StackError('Stack is empty')
    for token in token_list:
        if token not in operators:
            try:
                token = int(token)
            except:
                pass
            if not isinstance(token,int):
                raise TokenError(f'Unknown token: {token}')
        if isinstance(token,int):
            operand_stack.push(token)
        if token in operators:
            operand2 = operand_stack.pop()
            try:
                operand1 = operand_stack.pop()
            except IndexError:
                raise StackError('pop from empty list')
            result = do_math(token,operand1,operand2)
            operand_stack.push(result)
    answer = operand_stack.pop()
    if not operand_stack.is_empty():
        raise StackError('Stack is not empty')
    return answer
    ...


def do_math(operation: str, operand1: int, operand2: int) -> float:
    """Perform a math operation

    Note that an expression "1 2 /" means $2 / 1$, not $1 / 2$
    :param operation: arithmetic operation
    :param operand1: first operand
    :param operand2: second operand
    :return: the result of the operation
    >>> do_math("+", 1, 2)
    3
    >>> do_math("-", 1, 2)
    -1
    >>> do_math("*", 2, 3)
    6
    >>> do_math("/", 1, 2)
    0.5
    >>> do_math("//", 1, 2)
    0
    >>> do_math("**", 2, 3)
    8
    """
    # TODO: Implement this function
    operators = ['+','-','*','/','//','**','%']
    if operation not in operators:
        raise SyntaxError('invalid syntax')
    if operation == '+':
        return operand1 + operand2
    elif operation == '-':
        return operand1 - operand2
    elif operation == '*':
        return operand1 * operand2
    elif operation == '/':
        try:
            return operand1/operand2
        except ZeroDivisionError as zde:
            raise zde
    elif operation == '//':
        try:
            return operand1//operand2
        except ZeroDivisionError as zde:
            raise zde
    elif operation == '%':
        try:
            return operand1%operand2
        except ZeroDivisionError as zde:
            raise zde
    elif operation == '**':
        return operand1 ** operand2
    ...


def rpn_calc(filename: str) -> float:
    """Reverse Polish Notation calculator

    :param filename: name of the file to process
    :return: sum of the results of all *valid* expressions
    """
    # TODO: Implement this function
    f = open(filename,'r')
    lines = f.read().splitlines()
    sum = 0
    for line in lines:
        try:
            output = postfix_eval(line)
            result = output
            print(f"{line:60}{result}")
        except ZeroDivisionError as zde:
            error = f'ERROR: {zde}'
            print(f"{line:60}{error}")
        except StackError as se:
            error = f'ERROR: {se}'
            print(f"{line:60}{error}")
        if type(output)==int or type(output)==float:
            sum += output
            output = 0
    f.close()
    return round(sum,2)
    ...


def main():
    """Main function"""
    filename = "projects/rpn/rpn_1.in.txt"
    print(f"Processing {filename}")
    checksum = rpn_calc(filename)
    print(f"Checksum is {checksum:.2f}")
    print("*" * 30)
    filename = "projects/rpn/rpn_2.in.txt"
    print(f"Processing {filename}")
    checksum = rpn_calc(filename)
    print(f"Checksum is {checksum:.2f}")


if __name__ == "__main__":
    main()
