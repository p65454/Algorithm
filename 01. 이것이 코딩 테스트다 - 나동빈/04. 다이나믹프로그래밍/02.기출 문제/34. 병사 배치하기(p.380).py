# 34. 병사 배치하기(p.380)
# www.acmicpc.net/problem/18353
n = int(input())
array = list(map(int, input().split()))
result = 0

for i in range(n-1):
    if array[i] < array[i+1]:
        result += 1

if result == 0:
    result = 1

print(result)