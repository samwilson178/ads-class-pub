#!/usr/bin/env python3
"""
`bank` implementation and driver

@authors: Roman Yasinovskyy
@version: 2021.9
"""

from abc import ABC, abstractmethod
from decimal import Decimal


class Address:
    """Class Address"""

    def __init__(self, street: str, city: str, state: str, zip_code: str) -> None:
        """Initializer"""
        # TODO: Implement this method
        self._street = street
        self._city = city
        self._state = state
        self._zip = zip_code
        ...

    # TODO: Implement data members as properties
    @property
    def street(self):
        return self._street

    @property
    def city(self):
        return self._city

    @property
    def state(self):
        return self._state

    @property
    def zip(self):
        return self._zip
    ...

    def __repr__(self) -> str:
        """Address representation"""
        # TODO: Implement this method
        return f'Address({self._street}, {self._city}, {self._state}, {self._zip})'
        ...

    def __str__(self) -> str:
        """Address as a string"""
        # TODO: Implement this method
        return f"{self._street}\n{self._city}, {self._state} {self._zip}"
        ...

    def __eq__(self, other: object) -> bool:
        """Address comparison"""
        # TODO: Implement this method
        if self._street == other._street and self._city == other._city and self._state == other._state and self._zip == other._zip:
            return True
        ...

    @street.setter
    def street(self,new_street):
        self._street = new_street


class Customer:
    """Class Customer"""

    def __init__(self, name_init: str, dob_init: str, address_init: Address) -> None:
        """Initializer"""
        # TODO: Implement this method
        self._name = name_init
        self._dob = dob_init
        self._address = address_init
        ...

    # TODO: Implement data members as properties
    @property
    def name(self):
        return self._name

    @property
    def dob(self):
        return self._dob

    @property
    def address(self):
        return self._address
    ...

    def __repr__(self) -> str:
        """Customer representation"""
        # TODO: Implement this method
        return f"Customer({self._name}, {self._dob}, {self._address})"
        ...

    def __str__(self) -> str:
        """Customer as a string"""
        # TODO: Implement this method
        return f"{self._name} ({self._dob})\n{self._address}"
        ...

    def __eq__(self, other: object) -> bool:
        """Customer comparison"""
        # TODO: Implement this method
        if self._name == other._name and self._dob == other._dob and self._address == other._address:
            return True
        return False
        ...

    def move(self, new_address: Address) -> None:
        """Change address"""
        # TODO: Implement this method
        self._address = new_address
        ...


class Account(ABC):
    """Class Account"""

    @abstractmethod
    def __init__(self, owner: Customer, balance: Decimal = Decimal(0)):
        """Initializer"""
        # TODO: Implement this method
        self._owner = owner
        self._balance = balance
        ...

    # TODO: Implement data members as properties
    @property
    def owner(self):
        return self._owner

    @property
    def balance(self):
        return self._balance
    ...

    def __repr__(self) -> str:
        """Account representation"""
        # TODO: Implement this method
        return f"Account({self._owner}, {self._balance})"
        ...

    def __str__(self) -> str:
        """Account as a string"""
        # TODO: Implement this method
        return f'Account\nOwner: {self._owner}\nBalance: {self._balance:.2f}'
        ...

    def __eq__(self, other: object) -> bool:
        """Accounts comparison"""
        # TODO: Implement this method
        if self._owner == other._owner and self._balance == other._balance:
            return True
        return False
        ...

    def deposit(self, amount: Decimal) -> None:
        """Add money"""
        # TODO: Implement this method
        if amount <= 0:
            raise ValueError('Must deposit positive amount')
        self._balance += amount
        ...

    def close(self) -> None:
        """Close account"""
        # TODO: Implement this method
        self._balance = 0
        ...


class CheckingAccount(Account):
    """Class CheckingAccount"""

    def __init__(self, owner: Customer, fee: Decimal, balance: Decimal = Decimal(0)):
        """Initializer"""
        # TODO: Implement this method
        super().__init__(owner,balance)
        self._insufficient_funds_fee = fee
        ...

    # TODO: Implement data members as properties
    @property
    def fee(self):
        return self._insufficient_funds_fee
    ...

    def __repr__(self) -> str:
        """Checking account representation"""
        # TODO: Implement this method
        return f"CheckingAccount({self._owner}, {self._insufficient_funds_fee}, {self._balance})"
        ...

    def __str__(self):
        """Checking account as a string"""
        # TODO: Implement this method
        return f"Checking account\nOwner: {self._owner}\nBalance: {self._balance:.2f}"
        ...

    def __eq__(self, other: object) -> bool:
        """Checking accounts comparison"""
        # TODO: Implement this method
        if self._owner == other._owner and self._balance == other._balance:
            return True
        return False
        ...

    def process_check(self, amount: Decimal) -> None:
        """Processing a check"""
        # TODO: Implement this method
        if amount > self._balance:
            self._balance -= self._insufficient_funds_fee
            return
        self._balance -= amount
        ...


class SavingsAccount(Account):
    """Class SavingsAccount"""

    def __init__(
        self, owner: Customer, interest_rate: Decimal, balance: Decimal = Decimal(0)
    ):
        """Initializer"""
        # TODO: Implement this method
        super().__init__(owner,balance)
        self._annual_interest_rate = interest_rate
        ...

    # TODO: Implement data members as properties
    @property
    def interest(self):
        return self._annual_interest_rate
    ...

    def yield_interest(self) -> None:
        """Yield annual interest"""
        # TODO: Implement this method
        self._balance = self._balance * (1 + self._annual_interest_rate / 100)
        ...

    def __repr__(self) -> str:
        """Savings account representation"""
        # TODO: Implement this method
        return f"SavingsAccount({self._owner}, {self._annual_interest_rate}, {self._balance})"
        ...

    def __str__(self):
        """Savings account as a string"""
        # TODO: Implement this method
        return f"Savings account\nOwner: {self._owner}\nBalance: {self._balance:.2f}"
        ...

    def __eq__(self, other: object) -> bool:
        """Savings accounts comparison"""
        # TODO: Implement this method
        if self._owner == other._owner and self._balance == other._balance:
            return True
        return False
        ...


def main():
    """Entry point"""
    addr1 = Address("700 College Dr", "Decorah", "IA", "52101")
    addr2 = Address("100 Water St", "Decorah", "IA", "52101")

    print("Customer")
    cust = Customer("John Doe", "2021-03-11", addr1)
    print(cust)
    print("Customer moved")
    cust.move(addr2)
    print(cust)
    print("Address changed")
    addr2._street = "100 Short St"
    print(cust)


if __name__ == "__main__":
    main()
