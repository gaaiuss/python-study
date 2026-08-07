from abc import ABC, abstractmethod


class Material(ABC):
    def __init__(self, title: str, material_id: int) -> None:
        self.title = title
        self.material_id = material_id
        self.available = True

    @abstractmethod
    def borrow(self) -> bool: ...

    def return_material(self) -> None:
        print(f"{type(self).__name__} returned.")
        self.available = True

    def __repr__(self) -> str:
        cls_name = type(self).__name__
        attrs = f"{self.title!r}, {self.material_id!r}, {self.available!r}"
        return f"{cls_name}({attrs})"


class Book(Material):
    def __init__(self, title: str, material_id: int) -> None:
        super().__init__(title, material_id)
        self.borrow_limit = 14

    def borrow(self) -> bool:
        if self.available:
            print("Book borrowed, have a nice one.")
            self.available = False
            return True

        print("The book in question is not available at the moment.")
        return False


class Magazine(Material):
    def __init__(self, title: str, material_id: int, special_edition: int = 0) -> None:
        super().__init__(title, material_id)
        self.borrow_limit = 7
        self.special_edition = special_edition

    def borrow(self) -> bool:
        if self.special_edition:
            print("Sorry, this magazine is a special edition and cannot be borrowed.")
            return False
        if self.available:
            print("Magazine borrowed, have a nice one.")
            self.available = False
            return True

        print("The book in question is not available at the moment.")
        return False


if __name__ == "__main__":
    play = Magazine("Boy", 69)

    print(play.borrow())
    play.return_material()
    print(play.borrow())
    print(play.borrow())

    print(play)
