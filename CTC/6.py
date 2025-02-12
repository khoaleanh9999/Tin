def tinh_giai_thua(n):
    if n == 0:
        return 1
    else:
        giai_thua = 1
        for i in range (1, n + 1):
            giai_thua *= i
        return giai_thua
    
def tinh_to_hop(n, k):
    if k == 0 or k > n:
        return "Không hợp lệ"
    else:
        return tinh_giai_thua(n)