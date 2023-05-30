# https://www.acmicpc.net/problem/16234
from collections import deque

n, l, r = map(int, input().split())
array = []
for i in range(n):
    array.append(list(map(int, input().split())))
print(array)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(x, y):
    united = []
    united.append((x, y))
    visit[x][y] = True
    q = deque()
    q.append((x, y))
    cnt = 1
    total = array[x][y]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visit[nx][ny]:
                if l <= abs(array[nx][ny] - array[x][y]) <= r:
                    q.append((nx, ny))
                    visit[nx][ny] = True
                    total += array[nx][ny]
                    cnt += 1
                    united.append((nx, ny))
    for i, j in united:
        array[i][j] = total // cnt
    return cnt

result = 0
while True:

    visit = [[False for _ in range(n)] for _ in range(n)]
    temp = 0
    for i in range(n):
        for j in range(n):
            if not visit[i][j]:
                bfs(i, j)
                temp += 1
    if temp == n * n:
        break
    print('--------')
    result += 1
print(result)
