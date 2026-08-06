from typing import TYPE_CHECKING

from exercises.abstract_polimorfism_heritage.accounts import SavingsAccount

if TYPE_CHECKING:
    from exercises.abstract_polimorfism_heritage.accounts import Account


class Person:
    def __init__(self, name: str, age: int) -> None:
        self._name = name
        self._age = age

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        self._name = name

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, age: int) -> None:
        self._age = age

    def __repr__(self) -> str:
        cls_name = type(self).__name__
        attrs = f"{self.name!r}, {self.age!r}"
        return f"{cls_name}({attrs})"


class Client(Person):
    def __init__(self, name: str, age: int, account: Account) -> None:
        super().__init__(name, age)
        self.account = account


if __name__ == "__main__":
    account = SavingsAccount(123, 123)
    gaius = Client("Gaius", 23, account)

    print(gaius, account)
