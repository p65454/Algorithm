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




