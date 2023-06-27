import sys
ssr = sys.stdin.readline
n, m = map(int, ssr().split())
array = []
INF = int(1e9)
graph = [[INF] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, ssr().split())
    array.append((a, b))

for a in range(n+1):
    for b in range(n+1):
        if a == b:
            graph[a][b] = 0

for i in array:
    graph[i[0]][i[1]] = 1

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == INF:
            graph[i][j] = 0

for i in range(1, n+1):
    for j in range(i+1, n+1):
        if 0 < graph[i][j] or 0 < graph[j][i]:
            graph[j][i] += graph[i][j]
            graph[i][j] = graph[j][i]

for i in range(1, n+1):
    for j in range(1, n+1):
        print(graph[i][j], end=' ')
    print()

result = 0
for i in range(1, n+1):
    cnt = 0
    for j in range(1, n+1):
        if graph[i][j] != 0:
            cnt += 1
    if cnt == n - 1:
        result += 1

print(f'result = {result}')
'''
6 6
1 5
3 4
4 2
4 6
5 2
5 4
res = 1

3 2
1 2
2 3
res = 3

4 3
1 2
2 3
2 4
res = 2
'''