import time
from typing import final

# Another way to calculate time
"""another libary for time counter
from timeit import default_timer as timer
start = timer()
end = timer()
print(end - start)"""
# Another way to calculate time
"""
from datetime import datetime
start=datetime.now()
print = (datetime.now()-start)"""

i = 0
str1 = "test"
str2 = "file"
"""constant: final[int] = "hahaa"
print(constant)
constant = 'haha'
print(type(constant))"""


start = time.time()

for i in range(int(input('enter n term: '))):
    print(','.join(str2))
    print(f'hà tường nguyên')
    print(f'{1000000000:,}')
    print(f'{str1:#^10}')
    print(f'{str1:#<10}')
    print(f'{str1:#>10}')
    print(f'{str1:#^10}')
    print(f'{str1} + this file')
    print(f'this is {str1} {str2}')
    print("this is", str1, "file")
    print("this is {} {}".format(str1, str2))
    print(f'{"end":-^23}')

end = time.time()
print(end - start)

# Web
"""
https://quantrimang.com/hoc/ham-format-trong-python-165610
https://www.freecodecamp.org/news/python-print-variable-how-to-print-a-string-and-variable
"""