import math


class Fraction:

  def __init__(self, x, y):
    self.num = x
    self.den = y

  def __str__(self):
    return f"{self.num}/{self.den}"

  def __add__(self, other):
    new_num = self.num * other.den + other.num * self.den
    new_den = self.den * other.den
    return Fraction(new_num, new_den)

  def __sub__(self, other):
    new_num = self.num * other.den - other.num * self.den
    new_den = self.den * other.den
    return Fraction(new_num, new_den)

  def __mul__(self, other):
    new_num = self.num * other.num
    new_den = self.den * other.den
    return Fraction(new_num, new_den)

  def __truediv__(self, other):
    new_num = self.num * other.den
    new_den = self.den * other.num
    return Fraction(new_num, new_den)

  def convert_to_decimal(self):
    return self.num / self.den

  def simplify(self):
    gcd = math.gcd(self.num, self.den)
    simplified_num = self.num // gcd
    simplified_den = self.den // gcd
    return Fraction(simplified_num, simplified_den)


obj1 = Fraction(1, 2)
obj2 = Fraction(2, 6)

sum = obj1 + obj2
sub = obj1 - obj2
mul = obj1 * obj2
divi = obj1 / obj2

print(sum.simplify())
