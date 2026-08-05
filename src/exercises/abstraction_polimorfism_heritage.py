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
    Banco tem contas e clentes (Agregação)
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

    @abstractmethod
    def deposit(self, value: float) -> None: ...

    @abstractmethod
    def draw(self, value: float) -> None: ...


class CheckingAccount(Account):
    def __init__(self, agency: int, account_number: int) -> None:
        super().__init__(agency, account_number)
        self.limit = 1000.0

    def deposit(self, value: float) -> None:
        self.balance += value

    def _use_limit(self, new_balance: float) -> bool:
        return new_balance < 0

    def draw(self, value: float) -> None:
        new_balance = self.balance - value

        if self.balance < 0 and self.limit < 0:
            print("You cannot draw, no limit/balance available.")
        elif self._use_limit(new_balance):
            self.balance = new_balance
            self.limit += new_balance
        else:
            self.balance -= value


class SavingsAccount(Account): ...


class Person:
    def __init__(self) -> None:
        self._name = None
        self._age = None

    @property
    def name(self) -> str | None:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        self._name = name

    @property
    def age(self) -> int | None:
        return self._age

    @age.setter
    def age(self, age: int) -> None:
        self._age = age


class Client(Person):
    def __init__(self, account: Account) -> None:
        super().__init__()
        self.account = account


if __name__ == "__main__":
    check_acc = CheckingAccount(123, 123)
    # check_acc.deposit(100.0)
    check_acc.draw(1001.0)

    print(check_acc.__dict__)

    # gaius = Client(check_acc)
    # gaius.name = "Gaius"

    # print(gaius.__dict__)
