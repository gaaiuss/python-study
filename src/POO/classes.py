"""
Class is a frame to create other objects. Classes have attributes, methods (
class functions). The `__init__` method is used to set the first things the will
be runned in the class, like attributes.
"""


class Person:
    def __init__(self, name: str, surname: str) -> None:
        self.name = name
        self.surname = surname


person1 = Person("Caio", "G")
person2 = Person("Otávio", "Miranda")

print(person1.name, person1.surname, sep="\n")
print(person2.name, person2.surname, sep="\n")

"""
To access the class attributes you can use the method `__dict__` or vars(obj).
Be aware that this method are not read only, they can be editted as well.
Having a dict type class data, you can save it on a json file using dump.
"""

print(person1.__dict__)
person3 = Person(
    **person1.__dict__
)  # Unpacking the key value pair into the class attributes
