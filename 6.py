class Pow:
def my_pow(self, x: float, n: int) -> float:
"""
Computes x raised to the power n.
:param x: a float, the base
:param n: an integer, the exponent
:return: a float, x raised to the power n
"""
if n == 0:
return 1
elif n < 0:
return 1 / self.my_pow(x, -n)
elif n % 2 == 0:
return self.my_pow(x * x, n // 2)
else:
return x * self.my_pow(x, n - 1)