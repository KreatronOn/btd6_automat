class vec2:
    x: float = 0.0
    y: float = 0.0

    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def __add__(self, other):
        return vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return vector2(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return vector2(self.x * scalar, self.y * scalar)

class upgrade:
    a: int = 0
    b: int = 0
    c: int = 0