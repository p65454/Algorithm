# 34. 병사 배치하기(p.380)
# www.acmicpc.net/problem/18353
n = int(input())
array = list(map(int, input().split()))
result = 0

# for i in range(n-1):
#     if array[i] < array[i+1]:
#         result += 1
#
# if result == 0:
#     result = 1
d = [0] * (n+1)
temp = 0
for i in range(0, n-1):
    if array[i] < array[i+1]:
        d[i+1] = max(d[i], temp)
        for j in range(i+1, n-1):
            if array[j] > array[j+1]:
                temp += 1
    else:
        d[i] += 1

print(n - d[n])

