n = int (input("n = "))
s = 0
for i in range (5, n - 2):
    if n <= 3:
        break
    else:
        s += i
print (s)