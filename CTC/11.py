def sort_array():
    n = int(input("Nhập số phần tử của mảng (n <= 100): "))
    if n > 100:
        print("Số phần tử vượt quá giới hạn.")
        return
    arr = []
    for i in range(n):
        arr.append(int(input(f"Nhập phần tử thứ {i + 1}: ")))
    arr.sort()
    print(arr)