arr = list(map(int, input().split()))
k = 2

left = 0
odd_count = 0
max_length = 0

for right in range(len(arr)):
    if arr[right] % 2 != 0:
        odd_count += 1

    while odd_count > k:
        if arr[left] % 2 != 0:
            odd_count -= 1
        left += 1

    max_length = max(max_length, right - left + 1)

print("Longest length:", max_length)