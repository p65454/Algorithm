# https://www.acmicpc.net/problem/14502
n, m = map(int, input().split())
array = []
for _ in range(n):
    array.append(list(map(int, input().split())))
# for i in range(n):
#     print(array[i])
cnt = 3




# for i in range(n):
#     for a in range(0, m-2):
#         if array[i][a] == 0:
#             array[i][a] = 1
#         else:
#             continue
#
#         for b in range(a+1, m-1):
#             if array[i][b] == 0:
#                 array[i][b] = 1
#             else:
#                 continue
#
#             for c in range(b+1, m):
#                 if array[i][c] == 0:
#                     array[i][c] = 1
#                     bfs()
#                     array[i][c] = 0
#                 else:
#                     continue
#                 print(array)







"""
7 7
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0
# 27

4 6
0 0 0 0 0 0
1 0 0 0 0 2
1 1 1 0 0 2
0 0 0 0 0 2
#9

8 8
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
#3
"""