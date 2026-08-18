arr = list(map(int,input().split()))

k = 4
x = 10

window_sum = sum(arr[:k])
count = 0

if window_sum > x:
    count += 1

for i in range(k, len(arr)):
    window_sum += arr[i]
    window_sum -= arr[i - k]

    if window_sum > x:
        count += 1

print("Number of windows:", count)