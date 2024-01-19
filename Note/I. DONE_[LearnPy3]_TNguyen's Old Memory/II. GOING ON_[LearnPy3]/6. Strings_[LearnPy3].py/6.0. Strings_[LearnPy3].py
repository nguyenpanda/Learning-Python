# Strings:


# 'hello' is the same as "hello"
print("Hello\n")
print('Hello\n')

# Assign String to a Variable:
a = "Hello\n"
print(a)

# Multiline Strings:
b = """I love U
CH3CH2OH
E = mc**2.\n
"""
print(b)
c = '''I love U
CH3CH2OH
E = mc**2.'''
print(c)

# Strings are Arrays:
"""
Strings in Python are arrays of bytes representing unicode characters.
However, Python does not have a character data type, 
a single character is simply a string with a length of 1.
Square brackets can be used to access elements of the string.
"""
a = "Hello, World!"
print(a[1])

# Looping Through a String:
"""
Since strings are arrays, 
we can loop through the characters in a string, 
with a for loop.
"""
for x in "bananaaaa":
  print(x)
# result
"""
b
a
n
a
n
a
a
a
a
"""

# String Length:
a = "Hello, World! œ∑´®†"
print(len(a)) # result is 19 (include spacing, !@#$%^&≈∂®ƒ√©˙∆ and so on)

# Check String:
txt = "The best things in life are free!"
print("free" in txt) # result is True
print("haha" in txt) # result is False

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")
