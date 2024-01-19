# Modify Strings:


# Upper Case:
a = "1. Hello, World!"  # returns the string in upper case
print(a.upper())  # result: 1. HELLO, WORLD!

# Upper case the first character of the world
a = "2. hà tường nguyên đẹp trai vãi đái"
print(a.title())  # result: 2. Hà Tường Nguyên Đẹp Trai Vãi Đái

# Lower Case:
a = "3. Hello, World!"  # returns the string in lower case
print(a.lower())  # result: 2. hello, world!

# Remove Whitespace:
a = "  4. Hello, World!   "  # removes any whitespace from the beginning or the end
print(a.strip())  # result: 3. Hello, World!

# Replace String:
a = "5. Hello, World!"  # replaces a string with another string
print(a.replace("H", "J"))  # result: 4. Jello, World!

# Split String:
a = "6. Hello, World!, a, b. c"  # splits the string into substrings if it finds instances of the separator
print(a.split(","))  # result: ['5. Hello', ' World!', ' a', ' b. c']

