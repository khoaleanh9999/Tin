N = float(input("N = "))
sum = 0
sum += N % 10
N //= 10
sum += N % 10
N //= 10
sum += N
print (sum)