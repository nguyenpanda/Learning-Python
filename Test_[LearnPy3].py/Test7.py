import time


def delay(value):
    for count1 in range(value):
        for count2 in range(count1):
            pass


rocket = """

          /^\\
          |-|
          | |
          |N|
          |A|
          |S|
          |A|
         /| |\\
        / | | \\
       |  | |  |
        `-\"\"\"-`
"""

if __name__ == "__main__":
    jump_control = 0
    some_delay = 800
    shift_control = 0

    for i in range(30):
        print("\n")

    print(rocket)

    for i in range(30):
        delay(some_delay)
        time.sleep(some_delay / 1000)
        print("\n")
