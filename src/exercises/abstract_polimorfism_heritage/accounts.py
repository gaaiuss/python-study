from abc import ABC, abstractmethod


class Account(ABC):
    def __init__(self, agency: int, account_number: int, balance: float = 0) -> None:
        self.agency = agency
        self.account_number = account_number
        self.balance = balance

    def deposit(self, value: float) -> None:
        self.balance += value

    @abstractmethod
    def draw(self, value: float) -> None: ...


class CheckingAccount(Account):
    def __init__(
        self, agency: int, account_number: int, balance: float = 0, limit: float = 0
    ) -> None:
        super().__init__(agency, account_number, balance)
        self.limit = limit

    def draw(self, value: float) -> None:
        new_balance = self.balance - value
        max_limit = -self.limit

        if new_balance < max_limit:
            print("Insufficient balance/limit to draw.")
            return

        self.balance = new_balance


class SavingsAccount(Account):
    def draw(self, value: float) -> None:
        new_balance = self.balance - value

        if new_balance < 0:
            print("Insufficient balance to draw.")
            return

        self.balance = new_balance


if __name__ == "__main__":
    save_acc = CheckingAccount(123, 123, 0, 100)
    save_acc.deposit(50)
    save_acc.draw(50)
    save_acc.draw(50)
    save_acc.draw(50)
    save_acc.draw(50)

    print(save_acc.__dict__)
