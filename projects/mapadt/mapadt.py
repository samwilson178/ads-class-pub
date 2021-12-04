#!/usr/bin/env python3
"""
`mapadt` implementation and driver

@authors: Roman Yasinovskyy
@version: 2021.10
"""


from typing import Any, Union


class HashMap:
    """Class HashMap"""

    def __init__(self, size_init: int = 16):
        """
        Initialize HashTable

        :param size_init: maximum size of the map
        """
        # TODO: Implement this method
        self._size = size_init
        self._keys = [None]*self._size
        self._values = [None]*self._size
        ...

    def __setitem__(self, key: int, value: Any) -> None:
        """
        Setter

        :param key: key of the (new) item in the collection
        :param value: new value to be added to (or updated in) the collection
        """
        # TODO: Call `put`
        self.put(key,value)
        ...

    def put(self, key: int, value: Any) -> None:
        """
        Setter

        :param key: key of the (new) item in the collection
        :param value: new value to be added to (updated in) the collection
        :raise: MemoryError if the table is full
        """
        # TODO: Implement this method
        full = True
        for item in self._keys:
            if item == key or item == None:
                full = False
            
        if full == True:
            raise MemoryError('Hash Table is full')

        hash_value = self._hash(key)

        if self._keys[hash_value] is None:
            self._keys[hash_value] = key
            self._values[hash_value] = value
        else:
            if self._keys[hash_value] == key:
                self._values[hash_value] = value
            else:
                next_slot = self._rehash(hash_value)
                step = 0
                while self._keys[next_slot] is not None and self._keys[next_slot] != key and step < self._size:
                    next_slot = self._rehash(hash_value,step)
                    step +=1
                if self._keys[next_slot] is None:
                    self._keys[next_slot] = key
                    self._values[next_slot] = value
                else: 
                    self._values[next_slot] = value
        ...

    def __getitem__(self, key: int) -> Any:
        """
        Getter

        :param key: key of the item in the collection
        """
        # TODO: Call `get`
        ...
        return self.get(key)

    def get(self, key: int) -> Any:
        """
        Getter

        :param key: key of the item in the collection
        :raise: KeyError if the key is not found
        """
        # TODO: Implement this method
        start_slot = self._hash(key)
        position = start_slot
        counter = 1
        while self._keys[position] is not None:
            if self._keys[position] == key:
                return self._values[position]
            else:
                position = self._rehash(start_slot,counter)
                counter +=1
                if position == start_slot:
                    raise KeyError(f'There is no such key in the map: {key}.')
        raise KeyError(f'There is no such key in the map: {key}.')
        ...

    def __len__(self) -> int:
        """
        Map size

        :return: a number of key-value pairs stored in the collection
        """
        # TODO: Implement this method
        counter = 0
        for item in self._keys:
            if item != None:
                counter += 1
        return counter
        ...

    def __contains__(self, key: int) -> bool:
        """
        key in HashMap

        Check if the key is in the collection
        :param key: key of an item in the collection
        :return: `True` if the key is found, `False` otherwise
        """
        # TODO: Implement this method
        for item in self._keys:
            if item == key:
                return True
        return False
        ...

    def __str__(self) -> str:
        """
        String representation of the collection

        :return: collections as a string
        """
        # TODO: Implement this method
        items = {}
        counter = 0
        for i in self._keys:
            if i != None:
                items[i] = self._values[counter]
            counter += 1
        return str(items)
        ...

    def _hash(self, key: int) -> int:
        """
        Hash function

        Simple remainder
        :param key: key of an element
        """
        # TODO: Implement this method
        return key%self._size
        ...

    def _rehash(self, old_hash: int, step: int = 1) -> int:
        """
        Rehash function

        Use quadratic probing
        :param old_hash: old hash value
        :param step: step (1 by default)
        :return: new hash
        """
        # TODO: Implement this method
        return (old_hash+step**2)%self._size
        ...

    def keys(self) -> list[int]:
        """
        Keys in the collection

        :return: all keys
        """
        # TODO: Implement this method
        key_list = []
        for item in self._keys:
            if item is not None:
                key_list.append(item)
        return key_list
        ...

    def values(self) -> list[Any]:
        """
        Values in the collection

        :return: all values
        """
        # TODO: Implement this method
        value_list = []
        for item in self._values:
            if item is not None:
                value_list.append(item)
        return value_list
        ...

    def items(self) -> list[tuple[int, Any]]:
        """
        Items (key: value) in the collections

        :return: all items
        """
        # TODO: Implement this method
        items_list = []
        for i in range(0,self._size):
            if self._keys[i] != None:
                items_list.append((self._keys[i],self._values[i]))
        return items_list
        ...


def main():
    map = HashMap(5)
    print("Map (empty)")
    print("Expected output: {}")
    print(f"Produced output: {map}")

    print("Adding items")
    map[18] = "ant"
    map[61] = "bee"
    map.put(20, "cat")
    map.put(21, "deer")

    print("Retrieval")
    print("Expected output: ant")
    print(f"Produced output: {map[18]}")
    print("Expected output: deer")
    print(f"Produced output: {map[21]}")

    print("Updating")
    map[21] = "dog"
    print("Expected output: dog")
    print(f"Produced output: {map[21]}")

    print("Map (str)")
    print("Expected output: {20: 'cat', 61: 'bee', 21: 'dog', 18: 'ant'}")
    print(f"Produced output: {map}")

    print("Contains")
    print("Expected output: True")
    print(f"Produced output: {18 in map}")
    print("Expected output: False")
    print(f"Produced output: {81 in map}")

    print("Size")
    print("Expected output: 4")
    print(f"Produced output: {len(map)}")

    print("Keys (raw)")
    print("Expected output: [20, 61, 21, 18, None]")
    print(f"Produced output: {map._keys}")

    print("Keys (raw)")
    print("Expected output: [20, 61, 21, 18, None]")
    print(f"Produced output: {map._keys}")

    print("Keys (method)")
    print("Expected output: [20, 61, 21, 18]")
    print(f"Produced output: {map.keys()}")

    print("Values (raw)")
    print("Expected output: ['cat', 'bee', 'dog', 'ant', None]")
    print(f"Produced output: {map._values}")

    print("Values (method)")
    print("Expected output: ['cat', 'bee', 'dog', 'ant']")
    print(f"Produced output: {map.values()}")

    print("Items (method)")
    print("Expected output: [(20, 'cat'), (61, 'bee'), (21, 'dog'), (18, 'ant')]")
    print(f"Produced output: {map.items()}")


if __name__ == "__main__":
    main()
