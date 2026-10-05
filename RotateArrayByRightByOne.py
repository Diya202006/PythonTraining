def rotate_right_by_one(arr):
    last = arr[-1]

    for i in range(len(arr) - 1, 0, -1):
        arr[i] = arr[i - 1]

    arr[0] = last

n = int(input())
arr = list(map(int, input().split()))

rotate_right_by_one(arr)
print(*arr)