#!/usr/bin/env python3
"""
`morse` implementation and driver

@authors: Roman Yasinovskyy
@version: 2021.11
"""

import pathlib

from pythonds3.trees import BinaryTree


class Coder:
    """Morse code encoder and decoder"""

    def __init__(self, file_in: str):
        self.morse_tree = BinaryTree("")

        with open(file_in) as morse_file:
            for line in morse_file:
                letter, code = line.split()
                self.follow_and_insert(code, letter)

    def follow_and_insert(self, code_str: str, letter: str) -> None:
        """
        Follow the tree and insert a letter

        :param code_str: morse code sequence
        :param letter: letter corresponding to the `code_str`
        """
        # TODO: Implement this method
        current = self.morse_tree
        for char in code_str:
            if char == '.':
                if current.child_left == None:
                    current.insert_left('')
                current = current.child_left
            elif char == '-':
                if current.child_right == None:
                    current.insert_right('')
                current = current.child_right
        current.root = letter
        ...

    def follow_and_retrieve(self, code_str: str) -> str:
        """
        Follow the tree and retrieve a letter

        :param code_str: morse code sequence
        :return: letter corresponding to the `code_str`
        :raise: ValueError if the code is not found
        """
        # TODO: Implement this method
        current = self.morse_tree
        for char in code_str:
            if char == '.':
                if current.child_left == None:
                    raise ValueError(f"Could not find {code_str} in the tree")
                current = current.child_left
            elif char == '-':
                if current.child_right == None:
                    raise ValueError(f"Could not find {code_str} in the tree")
                current = current.child_right
        return current.get_root_val()
        ...

    def find_path(self, tree: BinaryTree, letter: str, path: str) -> str:
        """
        Find a path to the letter
        Encoder's helper function

        :param tree: Morse tree
        :param letter: letter to encode
        :param path: path to the letter
        :return: path to the letter
        """
        # TODO: Implement this method
        if tree == None:
            return False
        if tree.root == letter:
            return path
        else:
            return self.find_path(tree.child_left,letter,path+'.') or self.find_path(tree.child_right,letter,path+'-')
        ...

    def encode(self, msg: str) -> str:
        """
        Encode a message
        
        :param msg: text to encode
        :return: Morse code representation of the the message
        """
        # TODO: Implement this method
        msg_list = msg.split()
        code_str = []
        for word in msg_list:
            word_list = []
            for char in word:
                encoded = self.find_path(self.morse_tree,char,'')
                if encoded == False:
                    raise ValueError(f"Could not encode {msg}: {char} is not in the tree")
                word_list.append(encoded)
            code_str.append(' '.join(word_list))
        return " ".join(code_str)
        ...

    def decode(self, code: str) -> str:
        """
        Decode a message

        :param code: Morse code sequence to decode
        :return: text corresponding to the code
        """
        # TODO: Implement this method
        message = ''
        characters = code.split()
        for char in characters:
            try:
                message += self.follow_and_retrieve(char)
            except:
                raise ValueError(f"Could not decode {code}: {char} is not in the tree")
        return message
        ...


def main():
    """Main function"""
    filename = "morse.txt"
    if not pathlib.Path(filename).exists():
        filename = f"projects/morse/{filename}"
    morse_coder = Coder(filename)
    print("Encoding 'sos'")
    print("Expected: ... --- ...")
    print(f"Encoded : {morse_coder.encode('sos')}")
    print("---")
    print("Encoding 'data structures'")
    print("Expected: -.. .- - .- ... - .-. ..- -.-. - ..- .-. . ... ")
    print(f"Encoded : {morse_coder.encode('data structures')}")
    print("---")
    print("Encoding '$$'")
    print("Expected: Error message")
    try:
        print(f"Encoded : {morse_coder.encode('$$')}")
    except ValueError as value_err:
        print(f"ERROR: {value_err}")
    print("---")
    print("Decoding '.... . .-.. .-.. --- --..-- -.-. ... .---- -.... -----'")
    print("Expected: hello,cs160")
    test_str = ".... . .-.. .-.. --- --..-- -.-. ... .---- -.... -----"
    print(f"Decoded : {morse_coder.decode(test_str)}")


if __name__ == "__main__":
    main()
