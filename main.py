class Fraction:
  def __init__(self, x, y):
    self.num = x
    self.den = y

  def __str__(self):
    return f"{self.num}/{self.den}"




obj1 = Fraction(1,2)
print(obj1)