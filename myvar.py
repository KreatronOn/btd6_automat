class vec2:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def __add__(self, other):
        return vec2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return vec2(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return vec2(self.x * scalar, self.y * scalar)

    def __eq__(self, other):
        if not isinstance(other, vec2):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

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

    def __str__(self):
        return f"{self.a}, {self.b}, {self.c}"

    def __repr__(self):
        return f"upgrade({self.a}, {self.b}, {self.c})"

    def is_valid(self):
        low, mid, high = sorted((self.a, self.b, self.c))
        return low == 0 and mid <= 2 and high <= 5

    def _as_tuple(self, other):
        if isinstance(other, upgrade):
            return (other.a, other.b, other.c)
        return tuple(other)
    
    def _compare(self, other, op_func):
        other_tuple = self._as_tuple(other)
        valid_pairs = [(s, o) for s, o in zip(self, other_tuple) if s != 0 and o != 0]
        
        if not valid_pairs:
            return True 
            
        return all(op_func(s, o) for s, o in valid_pairs)

    def __lt__(self, other):
        return self._compare(other, lambda s, o: s < o)

    def __le__(self, other):
        return self._compare(other, lambda s, o: s <= o)

    def __gt__(self, other):
        return self._compare(other, lambda s, o: s > o)

    def __ge__(self, other):
        return self._compare(other, lambda s, o: s >= o)

    def __eq__(self, other):
        return self._compare(other, lambda s, o: s == o)