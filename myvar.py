class vec2:
    x: float = 0.0
    y: float = 0.0

    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def __add__(self, other):
        return vec2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return vec2(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return vec2(self.x * scalar, self.y * scalar)

class upgrade:
    a: int = 0
    b: int = 0
    c: int = 0

    def __init__(self, a=0, b=0, c=0):
        self.a = a
        self.b = b
        self.c = c

    def __iter__(self):
        return iter((self.a, self.b, self.c))

    def is_valid(self):
        low, mid, high = sorted((self.a, self.b, self.c))
        return low == 0 and mid <= 2 and high <= 5