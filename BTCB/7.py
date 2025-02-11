import math
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
print ("Chu vi = ", a + b + c)
p = (a + b + c) / 2
print ("Dien tich = ", math.sqrt(p * (p - a) * (p - b) * (p - c)))