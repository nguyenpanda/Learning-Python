# Global Variables:



""" 
Variables that are created outside of a function (as in all of the examples above) are known as global variables.
Global variables can be used by everyone, both inside of functions and outside.
"""
# 1. Global variables:
x = "awesome" # x is global variables
def myfunc1():
  print("1. Python is " + x)
myfunc1()
print(' ')



# 2. Local variables:
"""
If you create a variable with the same name inside a function, 
this variable will be local, and can only be used inside the function. 
The global variable with the same name will remain as it was, 
global and with the original value.
"""
x = "awesome"
def myfunc2():
  x = "fantastic" # Local variables
  print("2. Python is " + x)
myfunc2()
print("2. Python is " + x) # x inside the def is not the same as the x outside the def
print(' ')



# 3. The global Keyword:
"""
Normally, when you create a variable inside a function, that variable is local, 
and can only be used inside that function.
"""
#To create a global variable inside a function, you can use the global keyword.
x = "awesome"
def myfunc3():
  global x 
  x = "fantastic"
print(x)
myfunc3()
print("3. Python is " + x)
print(' ')

"""
Also, use the global keyword 
if you want to change a global variable inside a function
"""
x = "awesome"
def myfunc4():
  global x
  x = "fantastic"
myfunc4()
print("3.1. Python is " + x)
x = 'Change'
print(x)

# Result:
"""
1. Python is awesome
 
2. Python is fantastic
2. Python is awesome
 
awesome
3. Python is fantastic
 
3.1. Python is fantastic
Change
"""