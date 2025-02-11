import math
a = float (input(a = " "))
b = float (input(b = " "))
c = float (input(c = " "))
stamgiac = a + b + c
if (a + b > c and math.abs(a - b) < c):
    print ("a b c là cạnh tam giác")
else:
    print ("a b c không phai canh tam giác")