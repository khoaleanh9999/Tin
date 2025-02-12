def tinh_tong_day_so(n):
    if n < 0:
        return 0
    else:
        return n * (n + 1) // 2

n = int(input())
print(tinh_tong_day_so(n))