def count_even_odd(arr):
    even = 0
    odd = 0

    for num in arr:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1

    return even, odd
 
n = int(input())
arr = list(map(int, input().split()))

even, odd = count_even_odd(arr)
print(even, odd)