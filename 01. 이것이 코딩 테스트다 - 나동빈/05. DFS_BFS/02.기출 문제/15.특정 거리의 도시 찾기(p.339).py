# https://www.acmicpc.net/problem/18352
from collections import deque
n, m, k, x = map(int, input().split())
array = [[]]
graph = [[]]
for _ in range(m):
    array.append(list(map(int, input().split())))
for _ in range(n):
    graph.append([])
for _ in range(n-m):
    array.append([])


print(array)
print(graph)
for i in range(1, n+1):
    for j in range(1, n+1):
        if array[j] and array[j][0] == i:
            graph[i].append(array[j][1])




print(graph)
cnt = 0
def bfs(graph, x, visited):
    queue = deque([x])
    visited[x] = True
    result = []
    while queue:
        v = queue.popleft()
        temp = []
        #print(v, end=' ')
        for i in graph[v]:
            temp.append(i)

            if not visited[i]:
                queue.append(i)
                visited[i] = True
        result.append(temp)
        print(result)
    return result

visited = [False] * (n+1)
num_list = bfs(graph, x, visited)
print(num_list)


list_k = num_list[k-1]
for i in range(k-1):
    set_list = set(list_k) - set(num_list[i])
    list_k = set_list
print(list_k)
list_k = list(list_k)
list_k.sort()




if not list_k:
    print(-1)
else:
    for i in list_k:
        print(i, end='\n')

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




