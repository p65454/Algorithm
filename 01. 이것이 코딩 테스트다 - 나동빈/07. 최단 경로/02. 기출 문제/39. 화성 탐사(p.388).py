import heapq
import copy
def mars(array, distance, n):
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    start = (0, 0)
    queue = []
    #visited[0][0] = True
    heapq.heappush(queue, (array[0][0], start))
    while queue:
        dist, v = heapq.heappop(queue)
        x = v[0]
        y = v[1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if dist > distance[nx][ny]: # 이미 거리가 갱신 된 경우 무시
                    continue
                if dist + array[nx][ny] < distance[nx][ny]: # 이전 값이 더 작다면 새로 갱신 후 큐삽입
                    distance[nx][ny] = dist + array[nx][ny]
                    heapq.heappush(queue, (distance[nx][ny], (nx, ny)))
    return distance[n-1][n-1]


t = int(input())
result = []
for _ in range(t):
    n = int(input())
    array = []
    INF = int(1e9)
    distance = [[INF] * n for _ in range(n)]
    distance[0][0] = 0

    for _ in range(n):
        mars2 = list(map(int, input().split()))
        array.append(mars2)

    result.append(mars(array, distance, n))
for i in result:
    print(i)

'''
3
3
5 5 4
3 9 1
3 2 7
5
3 7 2 0 1
2 8 0 9 1
1 2 1 8 1
9 8 9 2 0
3 6 5 1 5
7
9 0 5 1 1 5 3
4 1 2 1 6 5 3
0 7 6 1 6 8 5
1 1 7 8 3 2 3
9 4 0 7 6 4 1
5 8 3 2 4 8 3
7 4 8 4 8 3 4

res = 
20
19
36
'''