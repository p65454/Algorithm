# https://www.acmicpc.net/problem/18428
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

#array_copy = copy.deepcopy(array)
for i in range(n):
    for j in range(n):
        if array[i][j] == 'S':
            s.append((i,j))
        elif array[i][j] == 'T':
            t.append((i,j))
        else:
            x.append((i,j))
num_s = len(s)
print(num_s)
print(s)
# 조합으로 장애물 3개 위치 설정
def comb_wall(wall):
    result = list(itertools.combinations(wall, 3))
    return result

cnt = 1
wall = comb_wall(x)
def run_T(t, array, wall):
    count_s_list = []
    for j in range(len(wall)):
        array_proto = copy.deepcopy(array)
        for k in range(3):
            a = wall[j][k][0]
            b = wall[j][k][1]
            array_proto[a][b] = 'O'
        for i in range(len(t)):
            x = t[i][0]
            y = t[i][1]
            temp = 0

            while True: #상
                nx, ny = x - (1 + temp), y
                if 0 <= nx < n and 0 <= ny < n and array_proto[nx][ny] != 'O' and array_proto[nx][ny] != 'T':
                    array_proto[nx][ny] = 'A'
                    temp += 1
                else:
                    temp = 0
                    break
            while True: #하
                nx, ny = x + (1 + temp), y
                if 0 <= nx < n and 0 <= ny < n and array_proto[nx][ny] != 'O' and array_proto[nx][ny] != 'T':
                    array_proto[nx][ny] = 'B'
                    temp += 1
                else:
                    temp = 0
                    break
            while True: #좌
                nx, ny = x, y - (1 + temp)
                if 0 <= nx < n and 0 <= ny < n and array_proto[nx][ny] != 'O' and array_proto[nx][ny] != 'T':
                    array_proto[nx][ny] = 'C'
                    temp += 1
                else:
                    temp = 0
                    break
            while True: #우
                nx, ny = x, y + (1 + temp)
                if 0 <= nx < n and 0 <= ny < n and array_proto[nx][ny] != 'O' and array_proto[nx][ny] != 'T':
                    array_proto[nx][ny] = 'D'
                    temp += 1
                else:
                    temp = 0
                    break
        for b in range(len(array_proto)):
            print(array_proto[b])
        print('---------------------------------')
        count_s = 0
        for a in range(len(array_proto)):
            count_s += array_proto[a].count('S')
        count_s_list.append(count_s)
    return count_s_list

result = run_T(t, array, wall)
print(result)
if num_s in result:
    print('YES')
else:
    print('NO')

'''
5
X S X X T
T X S X X
X X X X X
X T X X X
X X T X X
# YES

4
S S S T
X X X X
X X X X
T T T X
# NO

'''










