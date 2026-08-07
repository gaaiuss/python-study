from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from exercises.library.material import Material


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


class User(Person):
    def __init__(
        self, name: str, age: int, borrowed_materials: list[Material] | None = None
    ) -> None:
        super().__init__(name, age)
        self.borrowed_materials = borrowed_materials or []
