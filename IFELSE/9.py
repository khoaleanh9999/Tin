a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
max_num = a
min_num = b
if c > max_num:
    max_num = c
if c < min_num:
    min_num = c
print("Số l��n nhất:", max_num)
print("Số bé nhất:", min_num)