n = int(input())
d = []
for _ in range(n):
    d.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            d[i][j] = d[i-1][j] + d[i][j]
        elif j == i:
            d[i][j] = d[i - 1][j - 1] + d[i][j]
        else:
            d[i][j] = max(d[i-1][j-1], d[i-1][j]) + d[i][j]

result = max(d[n-1])
print(result)

