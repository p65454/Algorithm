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
result = []
x = 0

for i in range(n):
    for j in range(i, n):

        x = j
        temp_sum = 0
        print(f'j = {j}')
        while x < n:
            if x + t[x] <= n:
                temp_sum += p[x]
                x += t[x]
                print(f'x = {x}, temp_sum = {temp_sum}')
            else:
                x += 1
        result.append(temp_sum)
        print(result)

for i in range(n-1, -1, -1):
    for j in range(n-1, i-1, -1):
        x = j
        temp_sum = 0
        d = j + 1
        while x >= 0:
            if t[x] <= d - x:
                temp_sum += p[x]
                print(f'x = {x}, temp_sum = {temp_sum}')
                x -= 1
            else:
                x -= 1
        result.append(temp_sum)
        print(result)


print(max(result))







# 7
# 3 10
# 5 20
# 1 10
# 1 20
# 2 15
# 4 40
# 2 200