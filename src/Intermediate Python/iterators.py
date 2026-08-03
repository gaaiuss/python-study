"""
Iterable x Iterator
-------------------
Iterable have the responsibility to store the values that will be iterated.
Iterator just give you a value at a time, it only knows the next value of the
iterable.
"""

# Iterable -> Implements the __iter__ method (it has an iterator)
iterable = ["I", "have", "__iter__"]
# iterable.__iter__() and iter(iterable) are the same, returns the __iter__
# method from the iterable
iterator = iter(iterable)  # has the __iter__ and __next__ methods

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))  # StopIteration exception

"""
The iterator exhausts the values once it calls the 'next' method, it can never
access previous values. Nothing compels you from converting it in a list for
example.
The 'StopIteration' exception is the way how the 'for' loop knows when to stop.
"""
