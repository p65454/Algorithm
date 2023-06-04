from collections import deque
import sys

n, m, k, x = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)

print(graph)


def bfs(graph, start, visited):
    result = []
    cnt = 0
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        #result.append((cnt, v))
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

        result.append()
        cnt += 1
        print(queue)
    return result



visited = [False] * (n+1)

print(bfs(graph, x, visited))
