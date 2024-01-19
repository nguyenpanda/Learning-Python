# Assign Multiple Values:


# Many Values to Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
##########
print(' ')


# One Value to Multiple Variables
x = y = z = "Orange"
print(x)
print(y)
print(z)
##########
print(' ')


# Unpack a Collection
fruits = ["apple", "banana", "cherry"] # it like a var matrix
            #^       #^        #^ 
            #|       #|        #|
           #1st     #2nd      #3rd

x, y, z = fruits # x,y,z are assigned apple, banana, cherry, respectively

print(x)
print(y)
print(z)
##########


# Result:
"""                    
Orange
Banana
Cherry
                              
Orange
Orange
Orange
                              
apple
banana
cherry
"""