import sys
n, m = map(int, sys.stdin.readline().split())

def find_parent(parent, x):
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

parent = [0] * (n + 1)
for i in range(n+1):
    parent[i] = i
result = []
for i in range(m):
    check, a, b = map(int, sys.stdin.readline().split())
    if check == 0:
        union_parent(parent, a, b)
    else:
        if find_parent(parent, a) == find_parent(parent, b):
            result.append('YES')
        else:
            result.append('NO')
for i in result:
    print(i)


'''
7 8
0 1 3
1 1 7
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1
'''
