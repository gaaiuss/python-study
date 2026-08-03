"""
Create the Car class with a name.
Create the Engine class with a name.
Create the Manufacturer class with a name.
Associate Car with an Engine (an engine can be used by many cars).
Associate Car and Manufacturer (a manufacturer can make many cars).
Print the Car, Engine and Manufacturer name.
"""


class Car:
    def __init__(self, name: str) -> None:
        self.name = name
        self._manufacturer = None
        self._engine = None

    @property
    def engine(self) -> None | Engine:
        return self._engine

    @engine.setter
    def engine(self, name: str) -> None:
        self._engine = Engine(name, self)

    @property
    def manufacturer(self) -> None | Manufacturer:
        return self._manufacturer

    @manufacturer.setter
    def manufacturer(self, name: str) -> None:
        self._manufacturer = Manufacturer(name, self)


class Engine:
    def __init__(self, name: str, car: Car) -> None:
        self.name = name
        self._cars: list[Car] = []
        self._cars.append(car)


class Manufacturer:
    def __init__(self, name: str, car: Car) -> None:
        self.name = name
        self._cars: list[Car] = []
        self._cars.append(car)


fusca = Car("Fusca")
fusca.engine = "V8"
fusca.manufacturer = "Wolks"

print(fusca.name, fusca.engine.name, fusca.manufacturer.name)
