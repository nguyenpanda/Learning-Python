def my_decorator(function):
    def wrapper(*args, **kwargs):
        print("I am decorating your function!")
        function(*args, **kwargs)
        
    return wrapper

def hello_world_1(person):
    print (f"Hello {person}!")

# This is not an elegant ways
my_decorator(hello_world_1)('nguyen')

########################################

# Instead of using my_decorator(hello_world_1)(), we use decorator @
@my_decorator
def hello_world_2(person):
    print(f"Hello {person}!")

hello_world_2('nguyen')

########################################
######Practical Example 1: Logged#######
########################################
def logged(function):   
    def wrapper(*args, **kwargs):
        value = function(*args, **kwargs) 
        
        with open ('Lec2_result.txt', 'a+') as f:
            fname = function.__name__
            print (f" {fname} function returned value {value}") 
            f.write(f"{fname} function returned value {value}\n")
        
        return value

    return wrapper

@logged
def add(x, y):
    return x + y

print(add(10,20))

########################################
######Practical Example 2: Timing#######
########################################
import time

def timed(function):
    def wrapper(*args, **kwargs):
        start = time.time()
        value = function(*args, **kwargs)
        end = time.time()

        func_name = function.__name__
        print(f'{func_name} took {end - start} second to execute!')
        
        return value
    return wrapper

@timed
def my_function(num):
    for i in range(num):
        for j in range(num):
            print(i, j)

if __name__ == '__main__':
    my_function(100)