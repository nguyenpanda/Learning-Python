# Rules:


"""
1. A variable name MUST START with a letter or the underscore character
2. A variable name CANNOT START with a number
3. A variable name can ONLY CONTAIN alpha-numeric characters and underscores (A-z, 0-9, and _ )
4. Variable names are -SENSITIVE (age, Age and AGE are three different variables)
"""

# Example:
myvar = "Hà Tường Nguyên"
my_var = "Hà Tường Nguyên"
_my_var = "Hà Tường Nguyên" # If the var start with "_" symbol, VSC will change it into a faded color
myVar = "Hà Tường Nguyên"
MYVAR = "Hà Tường Nguyên" # If the var is capital writing, it will be ligher
myvar2 = "Hà Tường Nguyên"
MyVar = "Hà Tường Nguyên"

# Multi Words Variable Names:
myVariableName = "Panda"    # Camel Case
MyVariableName = "Panda"    # Pascal Case
my_variable_name = "Panda"  # Snake Case

# Error Example:
"""
2myvar = "Hà Tường Nguyên" ---> first rule
my-var = "Hà Tường Nguyên" ---> 3th rule
my var = "Hà Tường Nguyên" ---> 3th rule
"""