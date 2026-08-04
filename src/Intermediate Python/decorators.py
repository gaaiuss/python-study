# ruff: noqa: ANN201, ANN001, ANN003, ANN002, ANN202
# type:ignore
"""Decorator functions and decorators.

Decorate - Add / remove / restric / refactor
Decorator functions are functions that decorate others.
Decorators are used by Python for it to use decorator functions on another
funtions.
"""


def create_function(func):
    def intern(*args, **kwargs):  # This is the decorator function
        print("I am going to decorate you.")
        for arg in args:
            is_string(arg)

        print("OK, you were decorated.")
        return func(*args, **kwargs)

    return intern


def revert_string(string):
    return string[::-1]


def is_string(param):
    if not isinstance(param, str):
        msg = f"'{param}' must be str"
        raise TypeError(msg)


revert_string_checking_parameter = create_function(revert_string)
reversed_ = revert_string_checking_parameter("Caio")
print(reversed_)
