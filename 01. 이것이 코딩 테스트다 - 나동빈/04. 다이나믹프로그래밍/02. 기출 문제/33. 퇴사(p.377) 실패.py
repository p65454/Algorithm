# 33. 퇴사(p.377)
# www.acmicpc.net/problem/14501

n = int(input())
t = []
p = []
for i in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)

print(t)
print(p)
dp = [0] * (n + 1)
temp_sum = 0

for i in range(n-1, -1, -1):
    if t[i] + i <= n:
        dp[i] = max(p[i] + dp[t[i] + i], temp_sum)
        temp_sum = dp[i]

    else:
        dp[i] = temp_sum

print(dp)












# 7
# 3 10
# 5 20
# 1 10
# 1 20
# 2 15
# 4 40
# 2 200