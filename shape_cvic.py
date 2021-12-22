
"""
Tento modul poskytuje třídy Point a Circle.

>>> point = Point()
>>> point
Point(0, 0)
>>> point.x = 12
>>> str(point)
'(12, 0)'
>>> a = Point(3, 4)
>>> b = Point(3, 4)
>>> a == b
True
>>> a == point
False
>>> a != point
True

>>> circle = Circle(2)
>>> circle
Circle(2, 0, 0)
>>> circle.radius = 3
>>> circle.x = 12
>>> circle
Circle(3, 12, 0)
>>> a = Circle(4, 5, 6)
>>> b = Circle(4, 5, 6)
>>> a == b
True
>>> a == circle
False
>>> a != circle
True
"""

import math

class Point:

    def __init__(self, x=0, y=0):
        """2D kartézská souřadnice

        >>> point = Point()
        >>> point
        Point(0, 0)
        """
        self.x = x
        self.y = y


    def __add__(self, other):
        """Vrátí součet souřadnic dvou bodů

        >>> q = Point(1, 3)
        >>> r = Point(2, 4)
        >>> p = q + r
        >>> p
        Point(3, 7)
        """
        return Point(self.x + other.x, self.y + other.y)

    def __iadd__(self, other):
        """Vrátí součet souřadnic dvou bodů

        >>> q = Point(1, 3)
        >>> p = Point(2, 4)
        >>> p += q
        >>> p
        Point(3, 7)
        """
        return Point(self.x, self.y) + Point(other.x, other.y)

    def __sub__(self, other):
        """Vrátí rozdíl souřadnic dvou bodů

        >>> q = Point(5, 6)
        >>> r = Point(2, 4)
        >>> p = q - r
        >>> p
        Point(3, 2)
        """
        return Point(self.x - other.x, self.y - other.y)

    def __isub__(self, other):
        """Vrátí rozdíl souřadnic dvou bodů do původní proměnné

        >>> q = Point(2, 4)
        >>> p = Point(5, 6)
        >>> p -= q
        >>> p
        Point(3, 2)
        """
        return Point(self.x, self.y) - Point(other.x, other.y)

    def __mul__(self, n):
        """Vrátí násobek souřadnic bodu číslem

        >>> q = Point(1, 3)
        >>> p = q * 2
        >>> p
        Point(2, 6)
        """
        return Point(self.x * n, self.y * n)

    def __imul__(self, n):
        return Point(self.x * n, self.y * n)

    def __truediv__(self, n):
        """Vrátí podíl souřadnic bodu číslem

        >>> q = Point(4, 6)
        >>> p = q / 2
        >>> p
        Point(2.0, 3.0)
        """
        return Point(self.x / n, self.y / n)

    def __itruediv__(self, n):
        """Vrátí podíl souřadnic bodu číslem do původní proměnné

        >>> p = Point(4, 6)
        >>> p /= 2
        >>> p
        Point(2.0, 3.0)
        """
        return Point(self.x / n, self.y / n)

    def __floordiv__(self, n):
        """Vrátí podíl souřadnic bodu číslem

        >>> q = Point(5, 7)
        >>> p = q // 2
        >>> p
        Point(2, 3)
        """
        return Point(self.x // n, self.y // n)

    def __ifloordiv__(self, n):
        """Vrátí podíl souřadnic bodu číslem do původní proměnné

        >>> p = Point(5, 7)
        >>> p //= 2
        >>> p
        Point(2, 3)
        """
        return Point(self.x // n, self.y // n)

    def distance_from_origin(self):
        """Vrátí vzdálenost bodu od počátku

        >>> point = Point(3, 4)
        >>> point.distance_from_origin()
        5.0
        """
        return math.hypot(self.x, self.y)


    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


    def __repr__(self):
        return "Point({0.x!r}, {0.y!r})".format(self)


    def __str__(self):
        return "({0.x!r}, {0.y!r})".format(self)


class Circle(Point):

    def __init__(self, radius, x=0, y=0):
        """Kruh

        >>> circle = Circle(2)
        >>> circle
        Circle(2, 0, 0)
        """
        super().__init__(x, y)
        self.radius = radius


    def edge_distance_from_origin(self):
        """Vzdálenost okraje kruhu od počátku

        >>> circle = Circle(2, 3, 4)
        >>> circle.edge_distance_from_origin()
        3.0
        """
        return abs(self.distance_from_origin() - self.radius)


    def area(self):
        """Plocha kruhu

        >>> circle = Circle(3)
        >>> a = circle.area()
        >>> int(a)
        28
        """
        return math.pi * (self.radius ** 2)


    def circumference(self):
        """Obvod kruhu

        >>> circle = Circle(3)
        >>> d = circle.circumference()
        >>> int(d)
        18
        """
        return 2 * math.pi * self.radius


    def __eq__(self, other):
        return self.radius == other.radius and super().__eq__(other)


    def __repr__(self):
        return "Circle({0.radius!r}, {0.x!r}, {0.y!r})".format(self)


    def __str__(self):
        return repr(self)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
