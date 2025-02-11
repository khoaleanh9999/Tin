n = int (input("n = "))
if (n % 400 == 0) or (n % 4 == 0 and n % 100 != 0):
    print (n, "là năm nhuận")
else:
    print (n, "là năm không nhuận")