"""Write a class representing two-dimensional vector (with x and y coordinates), which supports the
following operations:
1. Addition of two vectors: v1 + v2
2. Subtraction of two vectors: v1 – v2
3. Dot product of two vectors:
    a. Using operator v1 * v2
    b. Using method v1.dot(v2)
    c. Using class method Vector2d.dot(v1, v2)
4. Vector length property:
    a. v.length
5. String representation: str(v) """
import math

# 4 a


class LengthDescriptor:
    def __get__(self, obj, obj_type):
        return math.sqrt(obj.x ** 2 + obj.y ** 2)


class Vector2d:

    length = LengthDescriptor()

    def __init__(self, x, y):
        self.x = x
        self.y = y

# 1
    def __add__(self, v2):
        result_x = self.x + v2.x
        result_y = self.y + v2.y
        return result_x, result_y

# 2
    def __sub__(self, v2):
        result_x = self.x - v2.x
        result_y = self.y - v2.y
        return result_x, result_y

# 3 a.
    def __mul__(self, v2):
        result_x = self.x * v2.x
        result_y = self.y * v2.y
        return result_x + result_y

# 3 b. c.
    def dot(self, v2):
        return self.__mul__(v2)

# 4 a

#     @property
#     def length(self):
#         return math.sqrt(self.x ** 2 + self.y ** 2)

# 5
    def __str__(self):
        return f'<{self.x}, {self.y}>'


ve1 = Vector2d(2, 4)
ve2 = Vector2d(3, 6)

print(ve1.length)
print(ve1 * ve2)
print(ve1 + ve2)
print(ve1 - ve2)
