# 실패 : 1 1 1 1 99 100 같은 경우의수를 생각 못하고 짰음

n = int(input())
home = list(map(int, input().split()))
home.sort()
sum_home = 0

for i in home:
    sum_home += i

avg = sum_home // n
print(avg)
new_home = []
for i in range(len(home)):
    new_home.append(abs(home[i] - avg))
new_home.sort()
sum_newhome = 0
for i in new_home:
    sum_newhome += i
new_avg = sum_newhome // n
ans1 = 0
ans2 = 0
print(home)
print(new_home)
print(new_avg)
if n <= 2:
    print(home[0])

else:
    for i in range(len(new_home)):
        if new_home[i] >= new_avg:
            ans1 = new_home[i]
            ans2 = new_home[i-1]
            break

    len_ans1 = 0
    len_ans2 = 0
    temp = 0
    print(f'ans1 = {ans1} ans2 = {ans2}')
    #각 경우의 거리계산
    for i in new_home:
        temp = abs(i - ans1)
        len_ans1 += temp

    for i in new_home:
        temp = abs(i - ans2)
        len_ans2 += temp

    min_value = min(len_ans1, len_ans2)
    print(len_ans1, len_ans2)
    print(min_value)
    result = []

    if min_value == len_ans1:
        result.append(ans1)
    if min_value == len_ans2:
        result.append(ans2)
    print(abs(min(result) - new_avg))





