x = float (input("x = "))
n = int (input("n = "))
s = 0
for i in range (1, n + 1):
    s += x ** i
print (s)