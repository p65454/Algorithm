s = list(map(int, input()))
new = []
res = 0
for i in range(len(s)-1):
    if s[i] != s[i+1]:
        new.append(s[i])
new.append(s[-1])
print(new)


if new.count(1) <= new.count(0):
    res = new.count(1)
else:
    res = new.count(0)

print(res)

