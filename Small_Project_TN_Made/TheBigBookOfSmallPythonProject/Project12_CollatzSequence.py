import sys as _sys
import time as _time

__all__ = ['collatz']

def collatz(number: int):
    print(number, end=' ', flush=True)
    while number != 1:
        if number % 2 == 0:
            number //= 2
        else:
            number = 3 * number + 1

        print(number, end=' ', flush=True)
        _time.sleep(0.1)
    print()

if __name__ == '__main__':
    if len(_sys.argv) != 2:
        _sys.exit(f'Usage: python CollatzSequence.py <Integer number>')

    if not _sys.argv[1].isdecimal():
        _sys.exit(f'U must enter a number')

    collatz(int(_sys.argv[1]))

