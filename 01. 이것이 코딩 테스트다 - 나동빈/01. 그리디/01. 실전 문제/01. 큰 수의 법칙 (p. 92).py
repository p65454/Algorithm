# 01. 큰 수의 법칙 (p. 92)

# input
n, m, k = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
sum = 0

while True:

    if m >= k:
        sum += num[n-1] * k
        m -= k
        if m >= 1:
            sum += num[n-2]
            m -= 1
        if m == 0:
            break
    else:
        sum += num[n-1] * m
        break

print(sum)