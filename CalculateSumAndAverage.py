def calculate_sum_average(arr):
    total = 0

    for num in arr:
        total += num

    avg = total / len(arr)

    return total, avg


# Input
n = int(input())
arr = list(map(int, input().split()))

total, avg = calculate_sum_average(arr)
print(total, avg)