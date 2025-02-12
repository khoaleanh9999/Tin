def tinh_tong_luy_nn(n):
    tong = 0
    for i in range (1,n + 1):
        tong += i ** i
    return tong