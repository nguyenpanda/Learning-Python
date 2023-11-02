def find_string_2():
    main_string = input("Enter your string: ")
    key_string = input("Enter the string you want to find: ")
    contain = []

    if (key_string in main_string) == True:
        first = main_string.find(key_string)
        contain.append(first)

        for i in range(len(main_string)):
            first = main_string.find(key_string, first + 1)
            contain.append(first)

            if first == -1:
                contain.pop()
                break

        print(f'Có {len(contain)} ký tự \"{key_string}\" \nVị trị của \"{key_string}\" bắt đầu từ 0 được sắp xếp trong list như sau:')
        print("->", contain)

    else:
        print('Ko có thấy má ơi')


def find_string_1():
    main_string = input("Enter your string: ")
    key_string = input("Enter the string you want to find: ")

    contain = []
    first = main_string.find(key_string)

    if first != -1:
        contain.append(first)

        for i in range(len(main_string)):
            if first == -1:
                break
            first = main_string.find(key_string, first + 1)
            contain.append(first)
        contain.remove(-1)

        print("Vị trí chữ \"{}\" của mày nè (mà nhớ là đếm tự số 0)".format(key_string))
        print("->", contain)

    else:
        print('Ko có thấy má ơi')


def factorial_2():  # Factorial of n (n!)
    # Note of factorial_2:
    """
    Maximum of n is 1558
    Faster than factorial_1

    If n overs 1558
    => ValueError: Exceeds the limit (4300) for integer string conversion;
                 use sys.set_int_max_str_digits() to increase the limit
    """
    n = int(input("Enter the integer of n value to calculate n!: "))

    factor = 1

    if n == 0:
        print(factor)
    while n < 0:
        n = int(input('Enter the positive integer number PLEASE: '))
    for i in range(n):
        factor = factor * (i + 1)
    print(f"The answer of {n}! is: ", factor)
    print(f"{n}! have", len(str(factor)), "digits")


def factorial_1():  # Factorial of n (n!)
    # note of factorial_1:
    """
    Maximum of n is 998
    Slower than factorial_2()

    If n overs 998:
    =>[Previous line repeated 996 more times]
        RecursionError: maximum recursion depth exceeded
    """
    x = int(input("Nhập số cần tính giai thừa: "))

    while x < 0:
        x = int(input("Làm ơn nhập số dương: "))

    def fact(x):
        if x == 0:
            return 1
        return x * fact(x - 1)

    print(fact(x))


def summation_1_over_n_series():
    # Sum of 1/1 + 1/2 + ... + 1/n
    n = int(input('Enter n number: '))

    while n <= 0:
        n = int(input('Enter the positive integer number PLEASE: '))

    sum = 0
    for i in range(n):
        i += 1
        sum = sum + 1 / i
    print(sum)


# factorial_1()
"""
    Maximum of n is 998
    Slower than factorial_2()
    
    If n overs 998:
    =>[Previous line repeated 996 more times]
        RecursionError: maximum recursion depth exceeded
    """
# factorial_2()
"""
    Maximum of n is 1558
    Faster than factorial_1
    
    If n overs 1558
    => ValueError: Exceeds the limit (4300) for integer string conversion;
                 use sys.set_int_max_str_digits() to increase the limit
    """
# summation_1_over_n_series()
"""

"""
# find_string_1()
"""

"""
# find_string_2()
"""

"""
