# 31.금광 (p.375)
t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    mine = list(map(int, input().split()))

    print(mine)

    d = []
    x = 0
    for i in range(n):
        d.append(mine[x : x + m])
        x += m

    print(d)
    for j in range(1, m):
        for i in range(n):
            if i == 0:
                d[i][j] = max(d[i][j-1], d[i+1][j-1]) + d[i][j]
            elif 0 < i < n-1:
                d[i][j] = max(d[i-1][j-1], d[i][j-1], d[i+1][j-1]) + d[i][j]
            else:
                d[i][j] = max(d[i-1][j-1], d[i][j-1]) + d[i][j]
    result = 0

    for i in range(n):
        result = max(result, d[i][m-1])

    print(result)




