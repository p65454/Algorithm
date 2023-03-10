from itertools import combinations

n, m = map(int, input().split())
k = list(map(int, input().split()))
result = len(list(combinations(k, 2)))

check = []   # 중복된 숫자 체크하기 위한 리스트
comb = []   # 중복된 숫자의 조합(combinations)을위한 리스트
for i in k:
    x = k.count(i)

    if x > 1:
        if i in check:
            continue

        else:
            check.append(i)
            for _ in range(x):
                comb.append(i)
            result -= len(list(combinations(comb, 2)))
            comb = []
print(result)
