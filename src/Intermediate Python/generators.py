"""Generators

Generators are functions that knows how to 'pause'. Every generator is an
iterator, you can navigate through (use the for loop etc), but an iterator is
not a generator.
Knowing this, like an iterator, the generator only knows its next value, getting
it one at a time.

In a list, for example, all the values are stored in the memory, so you can
access any value at any time you like.
Unlike the generator, that does not store any value in memory until you call for
the next value.
"""

from sys import getsizeof

list_ = [n for n in range(1000)]  # noqa: C416
generator = (n for n in range(1000))

"""
As the generator does not store any value in the memory, it will always have the
same size in memory.
"""
print(getsizeof(list_), "bytes")  # 8448728 bytes
print(getsizeof(generator), "bytes\n")  # 200 bytes

print(list_, "\n")  # the list stores all the values in the memory
print(generator)  # just give you a value at a time once you call for it

print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))

# You can use for in it too
for n in generator:
    print(n)
