#https://www.acmicpc.net/problem/18405
import sys
from collections import deque
n, k = map(int, sys.stdin.readline().split())
array = []
for i in range(n):
    array.append(list(map(int, sys.stdin.readline().split())))
s, x, y = map(int, sys.stdin.readline().split())

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# 0이 아닌 숫자들의 위치정보를 파악한 후 오름차순 정리
num_list = []
for i in range(n):
    for j in range(n):
        if array[i][j] != 0:
            num_list.append((array[i][j],0, i, j))
num_list.sort()
#print(num_list)

queue = deque(num_list)
while queue:
    number, sec, a, b = queue.popleft()
    if sec == s:
        break
    for i in range(4):
        nx = a + dx[i]
        ny = b + dy[i]
        if nx >= 0 and ny >= 0 and nx < n and ny < n:
            if array[nx][ny] == 0:
                array[nx][ny] = number
                queue.append((number, sec + 1, nx, ny))

# for i in range(len(array)):
#     print(array[i])

print(array[x-1][y-1])