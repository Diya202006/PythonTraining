arr = [10, 25, 5, 18, 40]

largest = arr[0]

for i in arr:
    if i > largest:
        largest = i

print("Largest Element:", largest)