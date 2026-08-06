from abc import ABC, abstractmethod


class Account(ABC):
    def __init__(self, agency: int, account_number: int) -> None:
        self.agency = agency
        self.account_number = account_number
        self.balance = 0.0

    def deposit(self, value: float) -> None:
        self.balance += value

    @abstractmethod
    def draw(self, value: float) -> None: ...


class CheckingAccount(Account):
    def draw(self, value: float) -> None:
        self.balance -= value


class SavingsAccount(Account):
    def draw(self, value: float) -> None:
        new_balance = self.balance - value

        if new_balance < 0:
            print("Insufficient balance to draw.")
            return

        self.balance = new_balance
