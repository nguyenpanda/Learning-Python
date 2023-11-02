from sympy import *

x = symbols('x')


def generate_variable_names(number_of_variables):
    var_name = []
    for i in range(0, number_of_variables):
        var_name.append(f"{'x'}{i}")

    return var_name

a = generate_variable_names(10)
print(a)


def assign_values_to_variables(variables, values):
    for i in range(len(variables)):
        exec(f"{variables[i]} = {values[i]}", globals())

    return variables

b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
assign_values_to_variables(a, b)


def multiply_polynomials(poly_coefficient_1, poly_coefficient_2):
    n = len(poly_coefficient_1)
    m = len(poly_coefficient_2)
    result = [0] * (n + m - 1)  # ['x0', 'x1', 'x2', 'x3', 'x4', 'x5', 'x6'] #

    for i in range(n):
        for j in range(m):
            # exec(f"{result[i + j]} == {poly_coefficient_1[i]}{poly_coefficient_2[j]}", globals())
            result[i + j] += poly_coefficient_1[i] * poly_coefficient_2[j]

    return result

T = [1, 2, 3]
B = [1, 2]

print(multiply_polynomials(T, B))


"""
#A = ['a0', 'a1', 'a2']
#B = ['b0', 'b1', 'b2']
#T = ['t0', 't1', 't2', 't3', 't4']

B = [1, 2, 3]
A = [1, 2, 3]
T = [1, 2, 3, 4, 5]
a = len(A)

C = ['x0', 'x1', 'x2', 'x3', 'x4', 'x5', 'x6'] # *(len(T) + len(B) - 1)

for t in range(len(T)-1):
    for b in range(len(B)-1):
        print(b)
        exec(f"{C[t + b]} == {T[t]}{B[b]}")
        print('Ha ha ha',x0)
"""


