def tinh_tong_giai_thua(n):
    tong = 0
    giai_thua = 1
    for i in range(1, n+1):
        giai_thua *= i
        tong += giai_thua
    return tong