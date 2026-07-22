arr = [1, 2, 4, 6, 7, 9]

for i in range(arr[0], arr[-1] + 1):
    if i not in arr:
        print(i)