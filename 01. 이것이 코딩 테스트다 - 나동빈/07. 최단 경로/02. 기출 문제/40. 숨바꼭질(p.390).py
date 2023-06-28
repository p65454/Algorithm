import heapq
n, m = map(int, input().split())
array = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    array[a].append(b)
    array[b].append(a)
print(array)
INF = int(1e9)
distance = [INF] * (n + 1)
start = 1

def hide_on_bush(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in array[now]:
            cost = dist + 1
            if cost < distance[i]:
                distance[i] = cost
                heapq.heappush(q, (cost, i))

hide_on_bush(start)
for i in range(len(distance)):
    if distance[i] == INF:
        distance[i] = 0

max_num = max(distance)
index = distance.index(max_num)
max_num_count = distance.count(max_num)
print(index, max_num, max_num_count)
# print(distance)

'''
6 7
3 6
4 3
3 2
1 3
1 2
2 4
5 2
res = 4 2 3
'''