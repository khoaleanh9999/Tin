n = int(input("n = "))
s = sum(1 / (i ** 2) for i in range(1, n + 1))
print(s)