def move_zeros_to_end(arr):
    pos = 0

    for i in range(len(arr)):
        if arr[i] != 0:
            arr[pos] = arr[i]
            pos += 1

    while pos < len(arr):
        arr[pos] = 0
        pos += 1


n = int(input())
arr = list(map(int, input().split()))

move_zeros_to_end(arr)
print(*arr)