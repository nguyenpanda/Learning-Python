class Vector:
    
    INPUT_TYPE = (float, int, complex)
    
    def __init__(self, x, y, z=None):
        assert isinstance(x, Vector.INPUT_TYPE), f'Error: x must be {Vector.input_type}, got {x}'
        assert isinstance(y, Vector.INPUT_TYPE), f'Error: y must be {Vector.input_type}, got {y}'
        assert isinstance(z, Vector.INPUT_TYPE), f'Error: z must be {Vector.input_type}, got {z}'
        self.x = x
        self.y = y
        if z is not None:
            self.z = z
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def __mul__(self,  other):
        if isinstance(other, Vector):
            return Vector(self.x * other.x, self.y * other.y, self.z * other.z)
        if isinstance(other, Vector.INPUT_TYPE):
            return Vector(self.x * other, self.y * other, self.y * other)
        
    def __eq__(self, __value: object) -> bool:
        if (self.x * __value.y == self.y * __value.x):
            return True
        else:
            return False
        
    def __len__(self)->int:
        return 10
    
    def __repr__(self) -> str:
        return f'{self.__class__.__name__} = ({self.x}, {self.y})'
    
    def __str__(self) -> str:
        return f'({self.x}, {self.y})'

v1 = Vector(1, 3, 3)

v2 = Vector(1, 3, 4)

v3 = Vector(1, 3, 4)

print(v1 + v2 + v3)
