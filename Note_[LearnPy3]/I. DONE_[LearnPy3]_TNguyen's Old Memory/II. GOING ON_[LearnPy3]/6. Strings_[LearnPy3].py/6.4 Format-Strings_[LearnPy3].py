# Format - Strings:


# String Format:
""" # TypeError: can only concatenate str (not "int") to str
age = 36
txt = "My name is John, I am " + age
print(txt)
"""

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
# result: My name is John, and I am 36

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
# result: I want 3 pieces of item 567 for 49.95 dollars.

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))
# result: I want to pay 49.95 dollars for 3 pieces of item 567.
