import math
n = int(input("n = "))
s = sum(math.factorial(i) for i in range(1, n + 1))
print(s)