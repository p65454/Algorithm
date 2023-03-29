n = int(input())
home = list(map(int, input().split()))

home.sort()
sum_home = 0

for i in home:
    sum_home += i

ans1 = 0
ans2 = 0
avg = sum_home / n
print(f'avg = {avg}')
if n <= 2:
    print(home[0])

else:
    for i in range(len(home)):
        if home[i] >= avg:
            ans1 = home[i]
            ans2 = home[i-1]
            break

    print(f'ans1 = {ans1} ans2 = {ans2}')
    result = []
    temp1 = 0
    temp2 = 0
    len_ans1 = 0
    len_ans2 = 0
    #각 경우의 거리계산
    for i in home:
        temp1 = abs(i - ans1)
        len_ans1 += temp1

    for i in home:
        temp2 = abs(i - ans2)
        len_ans2 += temp2

    min_value = min(len_ans1, len_ans2)
    print(len_ans1, len_ans2)
    print(min_value)

    if min_value == len_ans1:
        result.append(ans1)
    if min_value == len_ans2:
        result.append(ans2)

    print(min(result))

