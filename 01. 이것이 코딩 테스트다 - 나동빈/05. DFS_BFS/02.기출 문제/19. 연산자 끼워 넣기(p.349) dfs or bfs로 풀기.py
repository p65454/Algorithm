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

