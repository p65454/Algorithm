from collections import deque
import time
start = time.time()  # 시작 시간 저장
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
    is_end = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx > n-1 or ny > m-1:
                continue
            if graph[nx][ny] == 0:
                continue
            if nx == 0 and ny == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
                if nx == n-1 and ny == m-1:
                    queue.popleft()
                    is_end = 1
                    break
        if is_end == 1:
            break
    return graph[n-1][m-1]



print(bfs(0, 0))
for i in range(n):
    print(graph[i])
print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간
"""
5 6
101010
111111
000001
111111
111111
res = 10

5 6
111111
111111
111111
111111
111111
res = 10
"""



