#https://www.acmicpc.net/problem/14888
import itertools
import sys
from itertools import permutations
from collections import deque
n = int(input())
num_list = list(map(int, sys.stdin.readline().split()))
add, sub, mul, div = map(int, sys.stdin.readline().split())

work_list = []
for _ in range(add):
    work_list.append('a')
for _ in range(sub):
    work_list.append('s')
for _ in range(mul):
    work_list.append('m')
for _ in range(div):
    work_list.append('d')

print(num_list)
print(work_list)

work_permu = list(itertools.permutations(work_list, n-1))
print(work_permu)


# nq = deque(num_list)
# wq = deque(work_permu)
result = []

for j in range(len(work_permu)):
    temp = num_list[0]
    for i in range(n-1):
        if work_permu[j][i] == 'a':
            temp += num_list[i+1]
        if work_permu[j][i] == 's':
            temp -= num_list[i+1]
        if work_permu[j][i] == 'm':
            temp *= num_list[i+1]
        if work_permu[j][i] == 'd':
            if temp < 0:
                temp *= -1
                temp //= num_list[i+1]
                temp *= -1
            else:
                temp //= num_list[i+1]
    result.append(temp)
print(max(result))
print(min(result))
