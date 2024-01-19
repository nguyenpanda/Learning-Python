# Setting the Specific Data Type:



x0 = str("Hello World")	                            # str           
# 0. Hello World   

x1 = int(20)	                                    # int           
# 1. 20

x2 = float(20.5)                                 	# float         
# 2. 20.5

x3 = complex(1j)	                                # complex       
# 3. 1j 

x4 = list(("apple", "banana", "cherry"))	        # list          
# 4. ['apple', 'banana', 'cherry'] 

x5 = tuple(("apple", "banana", "cherry"))	        # tuple         
# 5. ('apple', 'banana', 'cherry') 

x6 = range(6)	                                    # range         
# 6. range(0, 6)

x7 = dict(name="John", age=36)	                    # dict          
# 7. {'name': 'John', 'age': 36}

x8 = set(("apple", "banana", "cherry"))	            # set           
# 8. {'apple', 'banana', 'cherry'}

x9 = frozenset(("apple", "banana", "cherry"))	    # frozenset     
# 9. frozenset({'apple', 'banana', 'cherry'})

x10 = bool(5)	                                    # bool          
# 10. True 

x11 = bytes(5)	                                    # bytes         
# 11. b'\x00\x00\x00\x00\x00'  

x12 = bytearray(5)	                                # bytearray     
# 12. bytearray(b'\x00\x00\x00\x00\x00') 

x13 = memoryview(bytes(5))	                        # memoryview    
# 13. <memory at 0x10d5b8a00>     


print(x0)
print(x1)
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


# Result:
"""
Hello World
20
20.5
1j
['apple', 'banana', 'cherry']
('apple', 'banana', 'cherry')
range(0, 6)
{'name': 'John', 'age': 36}
{'cherry', 'banana', 'apple'}
frozenset({'cherry', 'banana', 'apple'})
True
b'\x00\x00\x00\x00\x00'
bytearray(b'\x00\x00\x00\x00\x00')
<memory at 0x10b8e8a00>
"""
