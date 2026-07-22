arr = [10, 25, 5, 18, 40]

largest = second = float('-inf')

for i in arr:
    if i > largest:
        second = largest
        largest = i
    elif i > second and i != largest:
        second = i

print("Second Largest:", second)