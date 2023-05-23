# https://www.acmicpc.net/problem/18352
from collections import deque
import sys
n, m, k, x = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)

print(graph)

distance = [-1] * (n + 1)
distance[x] = 0

queue = deque([x])

while queue:
    v = queue.popleft()

    for i in graph[v]:
        if distance[i] == -1:
            distance[i] = distance[v] + 1
            queue.append(i)

print(distance)

check = False

for i in range(1, n+1):
    if distance[i] == k:
        check = True
        print(i)

if not check:
    print(-1)



# list_k = num_list[k-1]
# for i in range(k-1):
#     set_list = set(list_k) - set(num_list[i])
#     list_k = set_list
# print(list_k)
# list_k = list(list_k)
# list_k.sort()
#
#
#
#
# if not list_k:
#     print(-1)
# else:
#     for i in list_k:
#         print(i, end='\n')

# for i in num_list:
#     num_list2.append((i, num_list.count(i)))
#
# print(num_list2)
# num_list2 = set(num_list2)
#
# num_list2 = list(num_list2)
# num_list2.sort()
# print(num_list2)
# check = []
# for i in range(len(num_list2)):
#     if num_list2[i][1] == k:
#         check.append(k)
#         print(num_list2[i][0], end='\n')
# if not check:
#     print(-1)

"""
3 2 1 2
1 2
1 3
# -1

7 6 2 1
1 2
1 3
2 4
2 5
3 6
3 7
# 4
# 5
# 6
# 7

3 2 2 1
1 2
2 3
# 3

4 3 2 4
4 3
3 2
2 1
# 2

2 2 2 1
1 2
2 1
# -1

3 3 3 1
1 2
2 3
3 1
# -1

4 4 2 1
1 2
1 3
2 4
3 4
# 4

15 14 3 1
1 2
1 3
2 4
2 5
3 6
3 7
4 8
4 9
5 10
5 11
6 12
6 13
7 14
7 15
# 8
# 9
# 10
# 11
# 12
# 13
# 14
# 15

4 3 1 1
2 1
3 1
4 1
# -1

5 4 2 1
1 2
1 3
2 4
3 5
# 4
# 5

4 5 3 1
1 2
1 3
2 3
2 4
4 1
# -1

5 5 1 2
1 2
1 4
2 3
3 5
4 5
# 3

4 3 3 1
1 2
3 4
2 3
# 4

"""