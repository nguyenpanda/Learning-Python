# Slicing Strings:
"""
output_string = main_string[<starting>:<ending>]
    if starting blanks, it means the 0 index
    if ending blanks, it means the end of the string

-1 is the last character of the string
"""

# Slicing:
b = "Hello, World!"
print(b[2:5])  # result: llo (not include the final character which is 5)
# first character index is 0

# Slicing From the Start:
b = "Hello, World!"  # Get the characters from position 2 to position 5 (not included):
print(b[:5])  # result: Hello (first 5 digits)

# Slice To the End:
b = "Hello, World!"  # Get the characters from position 2, and all the way to the end:
print(b[2:])  # result: Hello (starting at the 2nd index)

# Negative Indexing:
b = "Hello, World!"
#           ^  ^
#           |  |
#          -6 -2
#           |  |
print(b[-6:-2])  # result: Worl (starting at -6 and ending at -2)


