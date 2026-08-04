"""
Generators are functions that knows how to 'pause'. Every generator is an
iterator, you can navigate through (use the for loop etc), but an iterator is
not a generator.

You use 'yield' to pause the execution until that point in a function, returning
a value. Like the iterators, you use 'next()' or '__next__' to call for the next
value or in this case, to pause on the next yield.
"""


def generator(n=0):
    yield 1  # Pause after this line
    print("Continue...")
    yield 2  # Pause
    print("Again...")
    yield 3
    print("Going to return")
    return "END"


gen = generator(n=0)
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

for n in gen:
    print(n)
