x = float(input("x = "))
y = float(input("y = "))
if (x * x + y * y <= 1):
    z = x * x + y * y
elif ((x * x + y * y > 1) and (y >= x)):
    z = x + y
else:
    z = 0.5
print (z)