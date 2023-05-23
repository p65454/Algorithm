from collections import deque
n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

print(graph)
dx = [0, 0, 1, -1]  # 상하우좌 ( 처음 간 곳 방문하는거 방지)
dy = [1, -1, 0, 0]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx > n-1 or ny > m-1:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    return graph[n-1][m-1]


print(bfs(0, 0))

# 5 6
# 101010
# 111111
# 000001
# 111111
# 111111
# res = 10

# 5 6
# 111111
# 111111
# 111111
# 111111
# 111111
# res = 10



