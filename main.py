from sympy import Symbol
from tests import generate_test_functions


def derivative(function, variable):
    return function.diff(variable)


def integrate(function, variable):
    return function.integrate(variable)


X = Symbol("x")
Y = Symbol("y")

test_list_width = 10
test_function_list = generate_test_functions(test_list_width)

print("-=" * 50)
print("DERIVADAS:")
for test_function in test_function_list.values():
    print(f"A derivada de ({test_function}) em relação à variável {X} é: {derivative(test_function, X)}")
    print(f"A derivada de ({test_function}) em relação à variável {Y} é: {derivative(test_function, Y)}")

print("-=" * 50)
print("INTEGRAIS:")
for test_function in test_function_list.values():
    print(f"A integral de ({test_function}) em relação à variável {X} é: {integrate(test_function, X)}")
    print(f"A integral de ({test_function}) em relação à variável {Y} é: {integrate(test_function, Y)}")
