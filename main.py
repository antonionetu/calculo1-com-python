from sympy import Symbol
import pickle

with open('functions.pickle', 'rb') as handle:
    test_function_list = pickle.load(handle)


def derivative(function, variable):
    return function.diff(variable)


def integrate(function, variable):
    return function.integrate(variable)


X = Symbol("x")
Y = Symbol("y")

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
