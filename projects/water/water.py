#!/usr/bin/env python3
"""
`water` implementation and driver

@authors:
@version: 2021.10
"""

JUG_1_MAX = 5
JUG_2_MAX = 3


class State:
    """State of the jugs"""

    def __init__(self, jug_1: int, jug_2: int) -> None:
        """Constructor"""
        # TODO: Implement this method
        if type(jug_1) != int or type(jug_2) != int:
            raise TypeError("__init__() should return None, not 'NotImplementedType'")
        if jug_1 > JUG_1_MAX:
            raise ValueError(f"The proposed value exceeds jug 1 capacity")
        self._jug_1 = jug_1
        if jug_2 > JUG_2_MAX:
            raise ValueError(f"The proposed value exceeds jug 2 capacity")
        self._jug_2 = jug_2
        ...

    

    def __eq__(self, other: object) -> bool:
        """Comparison for equality"""
        # TODO: Implement this method
        return self._jug_1 == other._jug_1 and self._jug_2 == other._jug_2
        ...

    def __repr__(self) -> str:
        """Object representation"""
        # TODO: Implement this method
        return f'State({self._jug_1},{self._jug_2})'
        ...

    def __str__(self) -> str:
        """Object as a string
        
        :return: a tuple of two jugs as a string
        """
        # TODO: Implement this method
        return f'({self._jug_1}, {self._jug_2})'
        ...

    def clone(self) -> 'State':
        """Copy a state

        :return: an identical copy (clone) of the State object
        """
        # TODO: Implement this method
        return State(self._jug_1,self._jug_2)
        ...

    def fill_jug_1(self):
        """Fill jug1 to capacity from the pump"""
        # TODO: Implement this method
        self._jug_1 = JUG_1_MAX
        return self
        ...

    def fill_jug_2(self):
        """Fill jug2 to capacity from the pump"""
        # TODO: Implement this method
        self._jug_2 = JUG_2_MAX
        return self
        ...

    def empty_jug_1(self):
        """Pour the water from jug1 onto the ground"""
        # TODO: Implement this method
        self._jug_1 = 0
        return self
        ...

    def empty_jug_2(self):
        """Pour the water from jug2 onto the ground"""
        # TODO: Implement this method
        self._jug_2 = 0
        return self
        ...

    def pour_jug_1_to_jug_2(self):
        """Pour as much water as you can from jug1 to jug2 without spilling"""
        # TODO: Implement this method
        max_pour = JUG_2_MAX - self._jug_2
        if self._jug_1 > max_pour:
            self._jug_1 -= max_pour
            self._jug_2 += max_pour
            return self
        self._jug_2 += self._jug_1
        self._jug_1 = 0
        return self
        ...

    def pour_jug_2_to_jug_1(self):
        """Pour as much water as you can from jug2 to jug1 without spilling"""
        # TODO: Implement this method
        max_pour = JUG_1_MAX - self._jug_1
        if self._jug_2 > max_pour:
            self._jug_2 -= max_pour
            self._jug_1 += max_pour
            return self
        self._jug_1 += self._jug_2
        self._jug_2 = 0
        return self
        ...


def search(start_state: State, goal: State, moves_lst: list):
    """Find a sequence of states"""
    # TODO: Implement this method
    if start_state in moves_lst:
        return False
    moves_lst.append(start_state)
    if start_state == goal:
        return moves_lst
    return (
        search(start_state.clone().fill_jug_1(),goal,moves_lst) or 
        search(start_state.clone().fill_jug_2(),goal,moves_lst) or 
        search(start_state.clone().empty_jug_1(),goal,moves_lst) or 
        search(start_state.clone().empty_jug_2(),goal,moves_lst) or 
        search(start_state.clone().pour_jug_1_to_jug_2(),goal,moves_lst) or 
        search(start_state.clone().pour_jug_2_to_jug_1(),goal,moves_lst)
        )
    ...
 

def main():
    """Main function"""
    goal = State(4, 0)
    start = State(0, 0)
    moves = []
    search(start, goal, moves)
    print(", ".join([str(s) for s in moves]))


if __name__ == "__main__":
    main()