# https://www.acmicpc.net/problem/2156


'''
입력
6
6
10
13
9
8
1
'''


# array = []
# for _ in range(7):
#     num = input()
#     array.append(num)
# print(array)

# dp = [[0, 0] for _ in range(n)]
# cnt = 0

# cnt = 1
# max_num = array[0]
# dp[0] = [cnt, max_num] 

# cnt = 2
# max_num = dp[0][1] + array[1]
# dp[1] = [cnt, max_num]

# cnt = 3
# if cnt == 3:
#     if dp[1][1] < array[2]:
#         max_num = dp[1][1] + array[2] - min(array[1], array[2])    
#     max_num = max(dp[1][1], (array[2] + max(array[1], array[2])))

# for i in range(1, len(array)):
    
def max_wine_amount(n, wine):
    if n == 1:
        return wine[0]
    if n == 2:
        return wine[0] + wine[1]
    
    dp = [0] * n
    dp[0] = wine[0]
    dp[1] = wine[0] + wine[1]
    dp[2] = max(wine[0] + wine[1], wine[0] + wine[2], wine[1] + wine[2])
    
    for i in range(3, n):
        dp[i] = max(dp[i-1], dp[i-2] + wine[i], dp[i-3] + wine[i-1] + wine[i])
    
    return print(dp[n-1])


# 출력
#max_wine_amount(n,wine)

n=int(input())

wine = []
for _ in range(n):
    num = int(input())
    wine.append(num)

max_wine_amount(n,wine)