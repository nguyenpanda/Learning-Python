# Dunder: double underscore __
from typing import Any, Callable


class Person:
    
    # This is the magic method
    def __init__(self, name, age, career) -> None:
        self.name = name
        self.age = age
        self.career = career

    def __del__(self):
        print('Object is being deconstructed!')


class Vector:
    
    INPUT_TYPE = (float, int, complex)
    
    def __init__(self, *args):
        self.__dimension = len(args)
        self.__value = list(args)

    def __add__(self, other):
        if isinstance(other, Vector):
            if self.__dimension != other.__dimension:
                raise TypeError(f'Different dimension, {self.__dimension} and {other.__dimension}')
            
            result_addition = [self.__value[i] + other.__value[i] for i in range(self.__dimension)]
            return Vector(*result_addition)
        
        elif isinstance(other, Vector.INPUT_TYPE):
            result_addition = [self.__value[i] + other for i in range(self.__dimension)]
            return Vector(*result_addition)
        
        else:
            raise TypeError(f'Unsupported operand type: {type(other)}')

    def __sub__(self, other):
        if isinstance(other, Vector):
            if self.__dimension != other.__dimension:
                raise TypeError(f'Different dimension, {self.__dimension} and {other.__dimension}')
            
            result_subtraction = [self.__value[i] - other.__value[i] for i in range(self.__dimension)]
            return Vector(*result_subtraction)
            
        elif isinstance(self, Vector.INPUT_TYPE):
            result_subtraction = [self.__value[i] - other for i in range(self.__dimension)]
            return Vector(*result_subtraction)
        
        else:
            raise TypeError(f'Unsupported operand type: {type(other)}')

    def __mul__(self, other):
        result_dot = 0
        if isinstance(other, Vector):
            if self.__dimension != other.__dimension:
                raise TypeError(f'Different dimension, {self.__dimension} and {other.__dimension}')
            
            for i in range(self.__dimension):
                result_dot += self.__value[i] * other.__value[i]            
            return result_dot
        
        elif isinstance(other, Vector.INPUT_TYPE):
            result_multiplication = [self.__value[i] * other for i in range(self.__dimension)]
            return Vector(*result_multiplication)
        
        else:
            raise TypeError(f'Unsupported operand type: {type(other)}')

    def __len__(self) -> int:
        return self.__dimension
    
    def __repr__(self) -> str:
        return f'{self.__class__.__name__}{tuple(self.__value)}'
    
    def __str__(self) -> str:
        return f'{tuple(self.__value)}'
    
    def dim(self):
        return self.__dimension
    
    def value(self, index: int):
        return self.__value[index-1]
    
if __name__ == '__main__':
    # Magic method is not called like regular method which object.some_method()
    person1 = Person('Nguyen', 19, 'Computer Science')
    del person1
    
    v1 = Vector(1, 2, 3)
    v2 = Vector(1, 2, 3)
    v3 = v1 + v2
    print(v3.value(1))
    