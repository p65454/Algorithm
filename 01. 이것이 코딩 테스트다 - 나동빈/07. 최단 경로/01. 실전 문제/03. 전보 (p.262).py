import heapq
import sys

n, m, c = map(int, sys.stdin.readline().split())
array = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y, z = map(int, sys.stdin.readline().split())
    array[x].append((y, z))

INF = int(1e9)
distance = [INF] * (n + 1)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in array[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
            print(q)


dijkstra(c)
cnt = 0
time = 0
for i in range(1, n + 1):
    if distance[i] < INF:
        cnt += 1
        time = max(time, distance[i])

print(cnt - 1, time)
print(distance)
