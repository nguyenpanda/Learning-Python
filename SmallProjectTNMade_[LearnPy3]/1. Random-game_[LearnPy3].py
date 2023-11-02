
import random


start = 1
end = 52
i = 0
random_number = random.randrange(start, end+1)

while random_number != 2:
    i += 1
    random_number = random.randrange(start, end+1)
    print(random_number)

print(i, "Time random to get it")
