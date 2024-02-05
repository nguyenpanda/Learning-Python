# Check ifError
def IfError(success, failure, *exceptions):
    try:
        return success()
    except exceptions or Exception:
        return failure


def my_expr():
    return 1/0

def iferror(success: str, failure, *exceptions):
    try:
        # Test
        return eval(success)

    except exceptions or Exception:
        return failure
print(iferror("1/0", "Hi there!"))

def IfError_2(true, false):
    try:
        print(int(9))
        raise ValueError()
    except ValueError:
        print("The string of text was not a number")
IfError(1, 2)
print(IfError(my_expr, 42))

# My test error
"""
try:
    x = 1/0
except IndexError:
    print('\nIndexError')

except TypeError:
    print('\nTypeError')

except ValueError:
    print('\nValueError')

except ZeroDivisionError:
    print('\nZeroDivisionError')

except ImportError:
    print('\nImportError')

except TimeoutError:
    print('\nTimeoutError')

except SyntaxError:
    print('\nSyntaxError')

except TabError:
    print('\nTabError')

# try:
#     print(1/0)
# except:
#     raise RuntimeError("Something bad happened")

# try:
#     print(int(e))
#     raise ValueError("Exception message")
# except ValueError as e:
#     print(str(e))
"""

"""
try:
    x = int(input("Enter "))
except ValueError:
    while ValueError:
        for i in range(1, 999):
            x = int(input("Enter "))
"""
