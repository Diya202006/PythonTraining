arr = [1, 2, 3, 2, 4, 5, 1, 6]

result = []

for i in arr:
    if i not in result:
        result.append(i)

print("Original List:", arr)
print("After Removing Duplicates:", result)