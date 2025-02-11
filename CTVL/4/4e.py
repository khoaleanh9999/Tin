x = float (input("x = "))
n = int (input("n = "))
s = 1
for i in range (n):
    if (n < 0):
        break
    else:
        s *= x
print (s)