import math
A = float(input("A = "))
B = float(input("B = "))
C = float(input("C = "))
xM = float(input("xM = "))
yM = float(input("yM = "))
d = abs(A * xM + B * yM + C) / math.sqrt(A * A + B * B)
print ("", d)