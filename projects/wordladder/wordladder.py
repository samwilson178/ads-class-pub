#!/usr/bin/env python3
"""
`wordladder` implementation and driver

@authors: Roman Yasinovskyy
@version: 2021.11
"""

import pathlib
import copy
from collections import deque
from pythonds3 import Stack,Queue



class Solver:
    """Build a ladder of words"""

    def __init__(self, filename: str):
        """Initialize sets of 3-, 4-, and 5-letter words"""
        self.words3: set[str] = set()  # 3-letter words
        self.words4: set[str] = set()  # 4-letter words
        self.words5: set[str] = set()  # 5-letter words
        # TODO: Implement this method
        f = open(filename,'r')
        words = f.read().splitlines()
        for line in words:
            if len(line) == 3:
                self.words3.add(line)
            elif len(line) == 4:
                self.words4.add(line)
            elif len(line) == 5:
                self.words5.add(line)
        ...

    def distance(self, word1: str, word2: str) -> int:
        """
        Find difference between words

        :param word1: 1st word
        :param word2: 2nd word
        :return: number of different letters in the same positions
        :raise: ValueError if words are not of the same length
        """
        # TODO: Implement this method
        if len(word1) != len(word2):
            raise ValueError('Must use words of the same length')
        dist = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                dist += 1
        return dist
        ...

    def diff_by_one_all(
        self, word: str, all_words: set[str], used_words: set[str]
    ) -> list[str]:
        """
        Find all words that differ by 1 letter

        :param word: target word
        :param all_words: all words of the same length as `word`
        :param used_words: all words that are already used and should not be considered
        """
        # TODO: Implement this method
        one_diff_words = []
        for cand in all_words:
            if cand not in used_words:
                if self.distance(word,cand) == 1:
                    one_diff_words.append(cand)
        return one_diff_words
        ...

    def build_ladder(self, word_start: str, word_stop: str) -> list[str]:
        """
        Build a word ladder

        :param word_start: 1st word
        :param word_stop: 2nd word
        :return a word ladder as a list
        """
        # TODO: Implement this method
        used_words = {word_start}
        if len(word_start) == 3:
            word_set = self.words3
        if len(word_start) == 4:
            word_set = self.words4
        if len(word_start) == 5:
            word_set = self.words5
        init_stack = Stack()
        init_stack.push(word_start)
        stack_queue = Queue()

        for word in self.diff_by_one_all(word_start,word_set,used_words):
            used_words.add(word)
            temp_stack = Stack()
            temp_stack._items = copy.deepcopy(init_stack._items)
            temp_stack.push(word)
            stack_queue.enqueue(temp_stack)

        found = False
        while found == False:
            try:
                check_stack = stack_queue.dequeue()
            except:
                return []
            if check_stack.peek() == word_stop:
                found = True
            else:
                for word in self.diff_by_one_all(check_stack.peek(),word_set,used_words):
                   temp_stack = Stack()
                   temp_stack._items = copy.deepcopy(check_stack._items)
                   temp_stack.push(word)
                   used_words.add(word)
                   stack_queue.enqueue(temp_stack)

        rev_stack = Stack()
        while check_stack.is_empty() == False:
            rev_stack.push(check_stack.pop())
        path_list = []
        while rev_stack.is_empty() == False:
            path_list.append(rev_stack.pop())

        return path_list
        ...


def main():
    """Main function"""
    filename = "words.txt"
    if not pathlib.Path(filename).exists():
        filename = f"projects/wordladder/{filename}"
    solver = Solver(filename)
    all_combinations = [
        ("elk", "elf"),
        ("elf", "elk"),
        ("odd", "peg"),
        ("tar", "pit"),
        ("milk", "mint"),
        ("memo", "koko"),
        ("myxo", "zuza"),
        ("snob", "rynd"),
        ("tenor", "xenon"),
        ("start", "spark"),
        ("camel", "amigo"),
        ("water", "stone"),
        ("abc", "xyz"),
        ("gizmo", "mulch"),
        ("tutor", "xenon"),
        ("peace", "piece"),
    ]
    for word_1, word_2 in all_combinations:
        print(f"Let's turn {word_1} into {word_2}")
        word_ladder = solver.build_ladder(word_1, word_2)

        if word_ladder:
            print("Ladder found!")
            print(" -> ".join(word_ladder))
        else:
            print("Ladder not found")


if __name__ == "__main__":
    main()
