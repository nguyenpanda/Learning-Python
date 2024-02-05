import time

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
    some_delay = 700
    shift_control = 0
    play_time = 50
    
    for i in range(10, -1, -1):
        print("\r{}".format(i), end="")
        time.sleep(0.3)
    
    print("\rRocket!!!")
    time.sleep(0.75)
    
    for i in range(30):
        print("\n")
    
    print(rocket)
    
    for i in range(play_time):
        time.sleep(some_delay / 1000)
        print("\n")
