# 37. 플로이드(p.385)
# https://www.acmicpc.net/problem/11404
import sys
ssr = sys.stdin.readline
n = int(ssr())
m = int(ssr())
INF = int(1e9)
array = [[INF] * (n + 1) for _ in range(n + 1)]

#INF = int(1e9)

for _ in range(m):
    a, b, c = map(int, ssr().split())
    if array[a][b] == INF:
        array[a][b] = c
    else:
        if array[a][b] > c:
            array[a][b] = c

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            array[a][b] = 0
# # print(array)
# for i in range(n+1):
#     print(array[i])

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            array[a][b] = min(array[a][b], array[a][k] + array[k][b])

for i in range(1, n+1):
    for j in range(1, n+1):
        if array[i][j] == INF:
            print('0', end=' ')
        else:
            print(array[i][j], end=' ')
    if i < n:
        print()

'''
5
14
1 2 2
1 3 3
1 4 1
1 5 10
2 4 2
3 4 1
3 5 1
4 5 3
3 5 10
3 1 8
1 4 2
5 1 7
3 4 2
5 2 4

res = 
0 2 3 1 4
12 0 15 2 5
8 5 0 1 1
10 7 13 0 3
7 4 10 6 0
'''