def tinh_tong_luy_thua_mn(m, n):
    tong = 0
    for i in range(1, m+1):
        tong += i ** n
    return tong