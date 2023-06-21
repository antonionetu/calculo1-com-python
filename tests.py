from sympy import Symbol, sin, cos, tan
from random import randint

Y = Symbol("y")
X = Symbol("x")


def generate_test_functions(list_width):
    functions = {}

    for count in range(1, list_width + 1):
        function_name = f"function_{count:02d}"
        rand_num = randint(1, 6)
        if rand_num == 1:
            functions[function_name] = X ** count
        elif rand_num == 2:
            functions[function_name] = Y ** count
        elif rand_num == 3:
            functions[function_name] = sin(X) ** count
        elif rand_num == 4:
            functions[function_name] = cos(Y) ** count
        elif rand_num == 5:
            functions[function_name] = tan(X) ** count
        else:
            functions[function_name] = X * Y ** count

    return functions

