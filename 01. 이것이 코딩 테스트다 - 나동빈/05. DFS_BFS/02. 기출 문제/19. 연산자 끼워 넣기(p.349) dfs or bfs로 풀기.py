#https://www.acmicpc.net/problem/14888
import itertools
import sys
from itertools import permutations
from collections import deque
n = int(input())
num_list = list(map(int, sys.stdin.readline().split()))
add, sub, mul, div = map(int, sys.stdin.readline().split())
max_value = -1e9
min_value = 1e9
def dfs(i, now):
    global max_value, min_value, add, sub, mul, div
    if i == n:
        max_value = max(max_value, now)
        min_value = min(min_value, now)

    else:
        if add > 0:
            add -= 1
            dfs(i+1, now + num_list[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i+1, now - num_list[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i+1, now * num_list[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i+1, int(now / num_list[i]))
            div += 1

dfs(1, num_list[0])

print(max_value)
print(min_value)


