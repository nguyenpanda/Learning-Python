from constant import pi


#############################################################
# Some math fx
def round(input, decimal):
    var = 10 ** decimal
    return int(input * var) / var

def factorial(n: int):
    if n < 0:
        raise ValueError("Factorial is undefined for negative numbers.")

    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def combination(n: int, k: int):
    if n < 0 or k < 0:
        raise ValueError("Combination is undefined for negative numbers.")

    return int(factorial(n) / (factorial(n - k) * factorial(k)))

def permutation(n: int, k: int):
    if n < 0 or k < 0:
        raise ValueError("Permutation is undefined for negative numbers.")
    return int(factorial(n) / (factorial(n - k)))

#############################################################
# Calculus fx
def integral_trap(function, lower: int, upper: int, number_of_retangle: int):
    if number_of_retangle <= 0:
        raise ValueError("Number of intervals must be a positive integer.")

    dx = (upper - lower) / number_of_retangle
    integral_sum = 0.5 * (function(lower) + function(upper))

    for i in range(1, number_of_retangle):
        integral_sum += function(lower + i * dx)
    integral_sum *= dx

    return integral_sum

def derivative(function, point):
    dx = 10 ** -10
    result = (function(point + dx) - function(point)) / dx
    return result


#############################################################
# Trigonometric fuction
def sin(input, n):
    result = 0
    for i in range(0, n):
        result += pow(-1, i) * pow(input, 2 * i + 1) / factorial(2 * i + 1)
    return result


def arcsin(input, n):
    if input == 1:
        return pi / 2

    if input == -1:
        return - pi / 2

    result = 0
    for i in range(0, n):
        result += factorial(2 * i) * pow(input, 2 * i + 1) / ((4 ** i) * (factorial(i) ** 2) * (2 * i + 1))
    return result

def cos(input, n):
    result = 0
    for i in range(0, n):
        result += pow(-1, i) * pow(input, 2 * i) / factorial(2 * i)
    return result

def arccos(input, n):
    return pi / 2 - arcsin(input, n)

def tan(input, n):
    return sin(input, n) / cos(input, n)

def arctan(input, recommend_a_even_number):
    n = recommend_a_even_number
    result = 0
    for i in range(0, n):
        result += pow(-1, i) * pow(input, (2 * i + 1)) / (2 * i + 1)
    return result

def cot(input, n):
    return cos(input, n) / sin(input, n)

#############################################################
#
def ln(input, n):
    result = 0
    for i in range(1, n + 1):
        result += pow(-1, i + 1) * pow(input - 1, i) / i
    return result


def my_ln_trap(input):
    return integral_trap(lambda x: 1 / x, 1, input, 1000 + input ** 2)


"""a = [0, 2.4, 2.9, 3.2, 3.4, 3.5, 3.5, 3.4, 3.1, 2.1, 0]
b = [1, 2, 3]



v = [0, 11, 21, 29, 30, 31, 35, 36, 40, 41,
    49, 50, 20, 21,  6,  5,  1, 00, 00, 00,
    12, 30, 40, 57, 60, 60, 65, 59, 42, 47,
    43, 48, 46, 41, 20, 10, 00, 00, 12, 22, 0]

input = []

for i in range(0, len(v)):
    input.append(v[i] / 3.6)


def trap(input, length):
    n = len(input) - 1
    dx = length / n
    print(dx)
    sum: float = 0.5 * (input[0] + input[-1])
    for i in range(1, n):
        sum += input[i]
    sum = sum * dx
    return sum

# print(trap(a, 10))
# print(trap(b, 2))
print(trap(input, 600))"""

"""
https://softwarenotebook.com/2022/01/01/calculate-derivative-functions-in-python/
"""
