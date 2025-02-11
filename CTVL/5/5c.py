n = int(input("n = "))
s = sum(i * (i + 1) for i in range(1, n + 1))
print(s)