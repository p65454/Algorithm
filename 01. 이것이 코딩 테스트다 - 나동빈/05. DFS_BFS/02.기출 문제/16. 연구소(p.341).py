# https://www.acmicpc.net/problem/14502
import itertools, copy
from collections import deque
n, m = map(int, input().split())
array = []
for _ in range(n):
    array.append(list(map(int, input().split())))

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
def bfs(x, y, array_proto):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx > n-1 or ny > m-1:
                continue
            if array_proto[nx][ny] == 1:
                continue
            if array_proto[nx][ny] == 0:
                array_proto[nx][ny] = 2
                queue.append((nx, ny))
    return array_proto

# 벽 3개 세울곳의 좌표를 조합으로 구하기
zero_point = []
two_point = []
for i in range(n):
    for j in range(m):
        if array[i][j] == 0:
            zero_point.append((i, j))
        if array[i][j] == 2:
            two_point.append((i, j))
wall_comb = list(itertools.combinations(zero_point, 3))

size_safety = []
#조합에 따라 벽을 세우고(반복문) 바이러스를 퍼뜨린다(bfs)
for i in range(len(wall_comb)):
    array_proto = copy.deepcopy(array)

    for j in range(3):
        x = wall_comb[i][j][0]
        y = wall_comb[i][j][1]
        if array_proto[x][y] == 0:
            array_proto[x][y] = 1
    for k in range(len(two_point)):
        a = two_point[k][0]
        b = two_point[k][1]
        result = bfs(a, b, array_proto)
    summary = 0
    for l in range(n):
        summary += result[l].count(0)
    size_safety.append(summary)

print(max(size_safety))










# for i in range(n):
#     for a in range(0, m-2):
#         if array[i][a] == 0:
#             array[i][a] = 1
#         else:
#             continue
#
#         for b in range(a+1, m-1):
#             if array[i][b] == 0:
#                 array[i][b] = 1
#             else:
#                 continue
#
#             for c in range(b+1, m):
#                 if array[i][c] == 0:
#                     array[i][c] = 1
#                     bfs()
#                     array[i][c] = 0
#                 else:
#                     continue
#                 print(array)







"""
7 7
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0
# 27

4 6
0 0 0 0 0 0
1 0 0 0 0 2
1 1 1 0 0 2
0 0 0 0 0 2
#9

8 8
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
#3
"""