#https://www.acmicpc.net/problem/18428
import itertools, copy
import sys
from itertools import combinations
n = int(input())
array = []
for _ in range(n):
    array.append(list(map(str, sys.stdin.readline().split())))
for i in range(n):
    print(array[i])
s = []
t = []
x = []
dx = [0, 0, -1, 1]  # 우 좌 하 상
dy = [1, -1, 0, 0]
array_proto = copy.deepcopy(array)
for i in range(n):
    for j in range(n):
        if array[i][j] == 'S':
            s.append((i,j))
        if array[i][j] == 'T':
            t.append((i,j))
        else:
            x.append((i,j))

num_s = len(s)

# 조합으로 장애물 3개 위치 설정
def comb_wall(wall):
    result = list(itertools.combinations(wall, 3))
    return result

def spray_T(t, array_proto, wall):
    cnt = 0
    for i in range(len(t)):
        x = t[i][0]
        y = t[i][1]
        for j in range(n):
            while x - cnt > 0:

                array_proto[x][j] = 'T'
                array_proto[j][y] = 'T'
    return array_proto

wall = comb_wall(x)










