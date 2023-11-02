"""
pip install mypy
mypy Lec6_TypeHinting.py (to check type hint)
"""

from typing import Callable

def func(val: int):
    print(val)

func('Nguyen')
