#!/usr/bin/env python3
"""
`recursion` implementation and driver

@authors: Roman Yasinovskyy
@version: 2021.10
"""


def gcd(a: int, b: int) -> int:
    """Greatest Common Denominator

    :param a: a number
    :param b: another number
    :return: the greatest common denominator between `a` and `b`
    >>> gcd(1860, 2020)
    20
    >>> gcd(1861, 2021)
    1
    """
    # TODO: Implement this function
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
    ...


def diamond_ite(levels: int) -> None:
    """Print a diamond

    :param levels: number of levels in the diamond
    """
    # TODO: Implement this function
    width = 2*levels-1
    for x in range(1,levels+1):
        print('{:^{largeline}}'.format('*'*(2*x-1),largeline=width))
    for x in range(levels-1,0,-1):
        print('{:^{largeline}}'.format('*'*(2*x-1),largeline=width))
    ...

def triangle_up(level: int, max_level: int) -> str:
    if level == max_level:
        return '{:^{largeline}}'.format('*'*(2*level-1),largeline=2*max_level-1)
    else:
        return '{:^{largeline}}\n{nextline}'.format('*'*(2*level-1),largeline=2*max_level-1,nextline=triangle_up(level+1,max_level))
    ...

def triangle_down(level: int, max_level: int) -> str:
    if level == 1:
        return '{:^{largeline}}'.format('*'*(2*level-1),largeline=2*max_level-1)
    else:
        return '{:^{largeline}}\n{nextline}'.format('*'*(2*level-1),largeline=2*max_level-1,nextline=triangle_down(level-1,max_level))
    ...

def diamond_rec(levels: int) -> None:
    """Print a diamond

    :param levels: number of levels in the diamond
    """
    # TODO: Implement this function
    print(triangle_up(1,levels))
    print(triangle_down(levels-1, levels))
    ...


def hourglass_ite(levels: int) -> None:
    """Print a hourglass

    :param levels: number of levels in the diamond
    """
    # TODO: Implement this function
    width = 2*levels-1
    for x in range(levels,0,-1):
        print('{:^{largeline}}'.format('*'*(2*x-1),largeline=width))
    for x in range(2,levels+1):
        print('{:^{largeline}}'.format('*'*(2*x-1),largeline=width))
    ...


def hourglass_rec(levels: int) -> None:
    """Print a hourglass

    :param levels: number of levels in the diamond
    """
    # TODO: Implement this function
    print(triangle_down(levels,levels))
    print(triangle_up(2,levels))
    ...


def main():
    """Main function"""
    print(f"GCD of 1861 and 2021 is {gcd(1861, 2021)}")
    print(f"GCD of 1860 and 2020 is {gcd(1860, 2020)}")
    print("Diamond (iterative)")
    diamond_ite(5)
    print("Diamond (recursive)")
    diamond_rec(5)
    print("Hourglass (iterative)")
    hourglass_ite(5)
    print("Hourglass (recursive)")
    hourglass_rec(5)


if __name__ == "__main__":
    main()
