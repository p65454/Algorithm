s = input()
a = list(s)
print(a)
a.sort()

sum = 0
result = []

for i in range(len(a)):

    if ord(a[i]) < 65:
        sum += int(a[i])
    else:
        result.append(a[i])
result = ''.join(result)
result = result+str(sum)
print(result)
