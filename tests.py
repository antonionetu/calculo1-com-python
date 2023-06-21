from sympy import Symbol, sin, cos, tan
from random import randint
import pickle

Y = Symbol("y")
X = Symbol("x")

functions = {}
test_list_width = 10

for count in range(1, test_list_width):
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

with open("functions.pickle", "wb") as handle:
    pickle.dump(functions, handle, protocol=pickle.HIGHEST_PROTOCOL)
