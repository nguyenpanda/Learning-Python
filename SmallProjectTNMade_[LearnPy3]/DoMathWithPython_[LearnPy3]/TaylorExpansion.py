 #
# testTaylorExpansion.py
# Located at Python 3/🐍Learn Python/SmallProjectTNMade_[LearnPy3]/DoMathWithPython_[LearnPy3]/testTaylorExpansion.py
#
# Created by Hà Tường Nguyên on 03/04/2023
#


from sympy import diff, symbols, sin
from constant import power_series
from MyMathFunc import factorial as factorial

def taylor_coefficient(function, x0, n):
    coefficients = []
    for k in range(0, n + 1):
        coefficients.append(diff(function, x, k).subs(x, x0)/factorial(k))
    return coefficients

def taylor_series(function, x0, n, have_multiplication_sign):
    # Fine the coefficient of each term in Taylor series
    coefficient = taylor_coefficient(function, x0, n)

    # Adding '+' in front of the direct number
    taylor_formula = ''
    for k in range(0, n):
        # Checking step if coefficient is a direct number
        if coefficient[k] >= 0:
            coefficient[k] = f'{"+"}{coefficient[k]}'

        # Combining the coefficient and the x^k together
        if have_multiplication_sign:
            coefficient[k] = f'{coefficient[k]}{"*"}{power_series[k]}'
        else:
            coefficient[k] = f'{coefficient[k]}{power_series[k]}'
        taylor_formula = taylor_formula + coefficient[k]

    # Erase the unnecessary term
    new_taylor_formula = ''
    i = 0
    while i < len(taylor_formula):
        # Find the zero term
        if taylor_formula[i:i + 3] == '+0x':
            # Ignore "+0x"
            i += 3

            # Run to the next term
            while i < len(taylor_formula) and (taylor_formula[i].isdigit() or taylor_formula[i] == '/'):
                i += 1
        else:
            new_taylor_formula += taylor_formula[i]
            i += 1

    return new_taylor_formula

### Input
x = symbols('x')

function1 = sin(x)
staring_point = 0
order = 20

print('-------------------------\n')


### Main
print(taylor_series(function1, staring_point, order, False))
print('-------------------------')


"""
def taylor_coefficient(fx, x0, n):
    # Calculate the coefficients of each term in the Taylor series
    coefficients = [diff(fx, x, k).subs(x, x0) / factorial(k) for k in range(n + 1)]
    return coefficients


def taylor_series(fx, x0, n, have_multiplication_sign):
    # Get the coefficients of the Taylor series terms
    coefficients = taylor_coefficient(fx, x0, n)
    terms = []

    for k in range(n):
        coefficient = coefficients[k]

        # Add '+' in front of direct coefficients
        if coefficient >= 0:
            coefficient = f'+{coefficient}'

        # Combine the coefficient and x^k together
        if have_multiplication_sign:
            term = f'{coefficient}*x**{k}'
        else:
            term = f'{coefficient}x**{k}'

        terms.append(term)

    taylor_formula = ''.join(terms)

    # Remove unnecessary terms with zero coefficient
    new_taylor_formula = taylor_formula.replace('+0x', '')

    return new_taylor_formula


# Input
x = symbols('x')
function1 = x / (x**2 -5*x + 6)
starting_point = 0
order = 7

# Main
print('-------------------------')
print(taylor_series(function1, starting_point, order, False))
print('-------------------------')
"""