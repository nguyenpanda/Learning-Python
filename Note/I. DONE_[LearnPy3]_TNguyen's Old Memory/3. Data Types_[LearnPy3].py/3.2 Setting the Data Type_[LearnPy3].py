# Setting the Data Type:


x0 = "Hello World"	                          # str          
# 0. Hello World

x1 = 20	                                      # int          
# 1. 20

x2 = 20.5	                                  # float        
# 2. 20.5

x3 = 1j                                       # complex      
# 3. 1j

x4 = ["apple", "banana", "cherry"]	          # list         
# 4. ['apple', 'banana', 'cherry']

x5 = ("apple", "banana", "cherry")	          # tuple         # tuple same as list but it can't change the date inside like list variable
# 5. ('apple', 'banana', 'cherry')

x6 = range(6)	                              # range        
# 6. range(0, 6)

x7 = {"name" : "John", "age" : 36}	          # dict         
# 7. {'name': 'John', 'age': 36}

x8 = {"apple", "banana", "cherry"}	          # set          
# 8. {'banana', 'apple', 'cherry'}

x9 = frozenset({"apple", "banana", "cherry"}) # frozenset    
# 9. frozenset({'banana', 'apple', 'cherry'})

x10 = True	                                  # bool         
# 10. True

x11 = b"Hello"	                              # bytes        
# 11. b'Hello'

x12 = bytearray(5)                            # bytearray    
# 12. bytearray(b'\x00\x00\x00\x00\x00')

x13 = memoryview(bytes(5))	                  # memoryview   
# 13. <memory at 0x1009a8a00>

x14 = None	                                  # NoneType     
# 14. None


print(x1)
print(x0)
print(x2)
print(x3)
print(x4)
print(x5)
print(x6)
print(x7)
print(x8)
print(x9)
print(x10)
print(x11)
print(x12)
print(x13)
print(x14)


# Result:
"""
0. Hello World
1. 20
2. 20.5
3. 1j
4. ['apple', 'banana', 'cherry']
5. ('apple', 'banana', 'cherry')
6. range(0, 6)
7. {'name': 'John', 'age': 36}
8. {'banana', 'apple', 'cherry'}
9. frozenset({'banana', 'apple', 'cherry'})
10. True
11. b'Hello'
12. bytearray(b'\x00\x00\x00\x00\x00')
13. <memory at 0x1009a8a00>
14. None
"""