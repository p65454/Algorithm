# https://www.acmicpc.net/problem/1647
import sys
n , m = map(int, sys.stdin.readline().split())


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

parent = [0] * (n + 1)
for i in range(n + 1):
    parent[i] = i

result = 0
last = 0
edges = []
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    edges.append((c, a, b))
edges.sort()
print(edges)
for i in edges:
    cost, a, b = i
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        temp = cost
        print(result, cost)

print(result - temp)

'''
7 12
1 2 3
1 3 2
3 2 1
2 5 2
3 4 4
7 3 6
5 1 5
1 6 2
6 4 1
6 5 3
4 5 3
6 7 4
res = 8
'''