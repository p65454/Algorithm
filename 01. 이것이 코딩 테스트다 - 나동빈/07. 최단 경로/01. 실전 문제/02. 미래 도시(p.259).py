n, m = map(int, input().split())
array = []
for _ in range(m):
    way = list(map(int, input().split()))
    array.append(way)
x, k = map(int, input().split())
#print(array)

INF = int(1e9)
graph = [[INF] * (n + 1) for _ in range(n+1)]

for a in range(n+1):
    for b in range(n+1):
        if a == b:
            graph[a][b] = 0

for i in array:
    a = i[0]
    b = i[1]
    graph[a][b] = graph[b][a] = 1


for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


if graph[1][k] + graph[k][x] >= INF:
    print(-1)
else:
    print(graph[1][k] + graph[k][x])


# for i in range(n+1):
#     print(graph[i])


'''
5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5
# res = 3

4 2
1 3
2 4
3 4
# res = -1
'''