from typing import TYPE_CHECKING

from exercises.abstract_polimorfism_heritage import bank
from exercises.abstract_polimorfism_heritage.accounts import (
    CheckingAccount,
    SavingsAccount,
)
from exercises.abstract_polimorfism_heritage.person import Client

if TYPE_CHECKING:
    from exercises.abstract_polimorfism_heritage.accounts import Account


class Bank:
    def __init__(
        self,
        agencies: list[int] | None = None,
        accounts: list[Account] | None = None,
        clients: list[Client] | None = None,
    ) -> None:
        self.agencies = agencies or []
        self.accounts = accounts or []
        self.clients = clients or []

    def _agency_check(self, agency: int) -> bool:
        if agency in self.agencies:
            return True

        print(f"{agency} does not exist in this Bank")
        return False

    def _client_check(self, client: Client) -> bool:
        if client in self.clients:
            return True

        print(f"{client} does not exist in this Bank")
        return False

    def _account_check(self, account: Account) -> bool:
        if account in self.accounts:
            return True

        print(f"{account} does not exist in this Bank")
        return False

    def _client_account_check(self, client: Client, account: Account) -> bool:
        if client.account == account:
            return True

        print(f"{account} does not belong to the {client}")
        return False

    def auth(self, agency: int, client: Client, account: Account) -> bool:
        return (
            self._agency_check(agency)
            and self._client_check(client)
            and self._account_check(account)
            and self._client_account_check(client, account)
        )

    def __repr__(self) -> str:
        cls_name = type(self).__name__
        attrs = f"{self.agencies!r}, {self.clients!r}, {self.accounts!r}"
        return f"{cls_name}({attrs})"


if __name__ == "__main__":
    account = SavingsAccount(123, 123)
    check_acc = CheckingAccount(321, 321)

    gaius = Client("Gaius", 23, account)
    john = Client("John", 23, check_acc)

    bank = Bank()
    bank.agencies.extend([123, 321, 456])
    bank.accounts.extend([account, check_acc])
    bank.clients.extend([gaius, john])

    bank.auth(account.agency, john, account)
