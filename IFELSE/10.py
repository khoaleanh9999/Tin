a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
d = float(input("d = "))
max_num = a
min_num = a
if (b > max_num):
    max_num = b
if (c > max_num):
    max_num = c
if (d > max_num):
    max_num = d
if (b < min_num):
    min_num = b
if (c < min_num):
    min_num = c
if (d < min_num):
    min_num = d
print ("Số lớn nhất là", max_num)
print ("Số bé nhất là", min_num)