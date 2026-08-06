from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from exercises.abstract_polimorfism_heritage.accounts import Account


class Person:
    def __init__(self, name: str, age: int) -> None:
        self._name = name
        self._age = age

    @property
    def name(self) -> str:
        return self._name

    @property
    def age(self) -> int:
        return self._age


class Client(Person):
    def __init__(self, name: str, age: int, account: Account) -> None:
        super().__init__(name, age)
        self.account = account
