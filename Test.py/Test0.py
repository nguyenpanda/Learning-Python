
import functools

@functools.lru_cache(maxsize=1000)
def fibonacci(n: int) -> int:
    if n == 0 or n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


file = open('text.txt', 'a')
for i in range(1000):
    file.writelines(str(fibonacci(i)) + '\n')
