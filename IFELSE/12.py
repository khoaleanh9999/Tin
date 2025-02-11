import math
a = float (input("a = "))
b = float (input("b = "))
c = float (input("c = "))
dental = b * b - 4 * a *c
if (dental > 0):
    print ("x1 = ", ((-b - math.sqrt(dental)) / 2 * a))
    print ("x2 = ", ((-b + math.sqrt(dental)) / 2 * a))
elif (dental == 0):
    print ("x = ", (-b / 2 * a))
else:
    print ("Phương trình vô nghiệm")