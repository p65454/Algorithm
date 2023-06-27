from collections import deque
def mars(array, distance, visited, n):
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    start = (0, 0)
    queue = deque()
    visited[0][0] = True
    queue.append(start)
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny]:
                    continue
                queue.append((nx, ny))
                visited[nx][ny] = True
                cost = distance[x][y]
                distance[nx][ny] = min(cost + array[nx][ny], array[x][y] + array[nx][ny])

    return distance


t = int(input())
for _ in range(t):
    n = int(input())
    array = []
    INF = int(1e9)
    distance = [[0] * n for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    for _ in range(n):
        mars2 = list(map(int, input().split()))
        array.append(mars2)

    for i in range(n):
        print(array[i])

    result = mars(array, distance, visited, n)
    for i in range(n):
        print(result[i])





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