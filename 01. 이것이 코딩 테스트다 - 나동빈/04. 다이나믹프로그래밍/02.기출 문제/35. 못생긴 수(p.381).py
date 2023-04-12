# 35. 못생긴 수(p.381)

n = int(input())
ugly = [0] * n
ugly[0] = 1

num2 = num3 = num5 = 0
next2, next3, next5 = 2, 3, 5

for i in range(1, n):
    ugly[i] = min(next2, next3, next5)

    if ugly[i] == next2:
        num2 += 1
        next2 = ugly[num2] * 2
    if ugly[i] == next3:
        num3 += 1
        next3 = ugly[num3] * 3
    if ugly[i] == next5:
        num5 += 1
        next5 = ugly[num5] * 5

print(ugly[n-1])











