arr = [1, 0, 2, 3, 0, 4, 0, 5]

result = []

zero_count = 0

for i in arr:
    if i == 0:
        zero_count += 1
    else:
        result.append(i)

for i in range(zero_count):
    result.append(0)

print(result)