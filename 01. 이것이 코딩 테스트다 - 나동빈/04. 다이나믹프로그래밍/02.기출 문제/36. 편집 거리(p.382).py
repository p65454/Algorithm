a = list(input())
b = list(input())
temp = [a[0]]
print(a, b)

dp = [0] * (len(b) + 1)
for i in range(len(b)):
    if temp[i] == b[i]:
        temp.append(b[i])
        dp[i] = 0
    else:
        if temp[i] not in b[i]:

            temp.pop(i)
            temp.insert(i, b[i])
        else:
            temp.insert(i, b[i])

