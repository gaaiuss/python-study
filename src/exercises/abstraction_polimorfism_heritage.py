"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra.

Conta (ABC)
    ContaCorrente
    ContaPoupanca

Pessoa (ABC)
    Cliente
        Clente -> Conta

Banco
    Banco -> Cliente
    Banco -> Conta

Dicas:
Criar classe Cliente que herda da classe Pessoa (Herança)
    Pessoa tem nome e idade (com getters)
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)
Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas têm agência, número da conta e saldo
    Contas devem ter método para depósito
    Conta (super classe) deve ter o método sacar abstrato (Abstração e
    polimorfismo - as subclasses que implementam o método sacar)
Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
Banco será responsável autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clientes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrita acima)
Banco autentica por um método.
"""

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


if __name__ == "__main__":
    check_acc = CheckingAccount(123, 123)
    sav_acc = SavingsAccount(234, 234)
    gaius = Client("Gaius", 26, check_acc)
    banco_bostil = Bank(123)

    banco_bostil.add_client(gaius)
    banco_bostil.add_account(check_acc, sav_acc)

    print(banco_bostil.__dict__)
