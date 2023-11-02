from MyMathFunc import *
from sympy import *

# Chuỗi Padé này em phải dùng thư viện ngoài để viết.

def calculate_pade_coefficients(func, m, n):
    x = symbols('x')

    # Define the Taylor series expansions
    taylor_expansion = func.series(x, 0, m + n + 1).removeO() #
    taylor_coeffs = [taylor_expansion.coeff(x, i) for i in range(m + n + 1)]

    # Write the rational fx form
    P_coeffs = symbols('a_0:%d' % (m + 1))
    Q_coeffs = symbols('b_0:%d' % (n + 1))
    P = sum(P_coeffs[i] * x ** i for i in range(m + 1))

    # Equate coefficients for P_coeffs
    P_equations = [Eq(taylor_coeffs[i], P.expand().coeff(x, i)) for i in range(m + 1)]
    P_solution = solve(P_equations, list(P_coeffs))

    # Substitute P_coeffs values and solve for Q_coeffs
    Q = Q_coeffs[0] + sum(Q_coeffs[i] * x ** i for i in range(1, n + 1))
    Q_equations = [Eq(0, Q.subs(P_solution).expand().coeff(x, i)) for i in range(1, n + 1)]
    Q_solution = solve(Q_equations, list(Q_coeffs[1:]))

    # Extract the coefficients
    P_coeff_values = [P_solution[coeff] for coeff in P_coeffs]
    Q_coeff_values = [Q_solution[coeff] for coeff in Q_coeffs[1:]]  # Exclude b_0 since it's known to be 1

    return P_coeff_values, Q_coeff_values


# Test Pade [m/n]
m = 2
n = 2
x = symbols('x')  # Define the variable x
sin_coeffs, cos_coeffs = calculate_pade_coefficients(sin(x), m, n)
print("Padé Approximant Coefficients for sin(x):")
print("P(x):", sin_coeffs)
print("Q(x):", [1] + cos_coeffs)  # Add 1 as the known coefficient b_0

# Bug
'''
18/05: TypeError line 3, 10, 19, 30
21/05: Like a taylor serie :")
'''