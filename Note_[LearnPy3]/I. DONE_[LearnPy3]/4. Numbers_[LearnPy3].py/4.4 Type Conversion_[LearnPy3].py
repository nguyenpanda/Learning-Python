# Type Conversion:


x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x) # Result: a = 1.0

#convert from float to int:
b = int(y) #it take the first digital of the float
# Result: b = 2

#convert from int to complex:
c = complex(x)
# Result: (1+0j)
d = complex(y)
# Result: (2.8+0j)

print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))


# Result:
"""
1.0 <class 'float'>
2 <class 'int'>
(1+0j) <class 'complex'>
(2.8+0j) <class 'complex'>
"""