import time
start = time.time()
for x in range(1, 21):
    # print('Replace the number on a single line: {}\r'.format(x), end="")
    print('Replace the number on a single line: {}\r'.format(x), end="")
    time.sleep(0.5)
end = time.time()
print("\n", end - start)

print("Helloooo \rWorld")
