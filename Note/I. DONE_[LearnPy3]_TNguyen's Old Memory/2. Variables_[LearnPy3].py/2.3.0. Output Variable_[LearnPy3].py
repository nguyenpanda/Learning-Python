# Output Variable:


# The Python print() function is often used to output variables.

# Assign a str by a var
x = "1. Python is awesome"
print(x)
##########
print(' ')

# Add str together
x = "2. Python"
y = "is"
z = "awesome"
print(x, y, z)
##########
print(' ')

x = "3. Python "
y = "is "
z = "awesome"
print(x + y + z)
##########
print(' ')

x0 = "4."
x = 5
y = 10
print(x0, x + y)
##########
print(' ')

# Error: different data types
"""
x = 5
y = "John"
print(x + y)
"""
##########

x0 = "5."
x = 5
y = "John"
print(x0, x, y) # Should USE "," TO COMBINE DIFFERENT TYPE OF DATA
print(' ')

x = 5
y = 10
z = 'haha'
print("The value of x, y and z are {}, {} and {}, respectively".format(x, y, z))


# Result:
"""
1. Python is awesome
 
2. Python is awesome
 
3. Python is awesome
 
4. 15
 
5. 5 John
 
The value of x, y and z are 5, 10 and haha, respectively
"""
