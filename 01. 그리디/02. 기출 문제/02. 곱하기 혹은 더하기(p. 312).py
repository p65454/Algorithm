s = list(map(int, input()))

sum = 0
print(s)
for i in range(len(s)):
    if s[i] == 1:
        sum += s[i]
    elif s[i] == 0:
        continue
    else:
        if sum == 0:
            sum += s[i]
        else:
            sum *= s[i]

print(sum)


