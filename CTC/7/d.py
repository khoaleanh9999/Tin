def tinh_tong_luy_thua_x(x, n):
    if x == 1:
        return n
    else:
        return (x * (x ** n - 1)) // x - 1 