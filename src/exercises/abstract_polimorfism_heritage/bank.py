from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from exercises.abstract_polimorfism_heritage.accounts import Account
    from exercises.abstract_polimorfism_heritage.clients import Client


class Bank:
    def __init__(self, agency: int) -> None:
        self.agency = agency
        self.accounts: list[Account] = []
        self.clients: list[Client] = []

    def add_client(self, *args: Client) -> None:
        for client in args:
            self.clients.append(client)

    def add_account(self, *args: Account) -> None:
        for account in args:
            self.accounts.append(account)

    def auth(self, client: Client, account: Account) -> bool:
        return (
            client in self.clients
            and account in self.accounts
            and self.agency == account.agency
        )
