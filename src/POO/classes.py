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
print()

"""
To access the class attributes you can use the method `__dict__` or vars(obj).
Be aware that this method are not read only, they can be editted as well.
Having a dict type class data, you can save it on a json file using dump.
"""

print(person1.__dict__)
person3 = Person(
    **person1.__dict__  # Unpacking the key value pair into the class attributes
)
print(person3.__dict__)
print()

"""
@classmethod is basically an extension of the class itself, you can use a method
directly from the class using the class as a parameter (cls), not the instance
(self) like a normal method from an object.
"""


class Animal:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    @classmethod
    def create_without_name(cls, age: int) -> Animal:  # using cls instead of self
        return cls("Anonymous", age)


lion = Animal("Lion", 20)
anonymous = Animal.create_without_name(30)

print(lion.__dict__)
print(anonymous.__dict__)
