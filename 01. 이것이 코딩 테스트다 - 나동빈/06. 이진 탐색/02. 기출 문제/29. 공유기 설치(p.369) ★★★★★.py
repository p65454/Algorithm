# https://www.acmicpc.net/problem/2110
n, c = map(int, input().split())
array = []
for _ in range(n):
    x = int(input())
    array.append(x)
array.sort()
max_gap = array[-1] - array[0]
min_gap = 1


def BTS(array, start, end):
    while(start <= end):
        mid = (start + end) // 2
        cnt = 1
        temp = array[0]
        for i in range(1,n):
            if array[i] - temp >= mid:
                temp = array[i]
                cnt += 1
        if cnt >= c:
            start = mid + 1
            result = mid
        else:
            end = mid - 1

        print(mid)
    return result

print(BTS(array, min_gap, max_gap))


'''
12 3
1
2
3
4
5
6
7
8
700
800
900
1000
# 300
-----------------------
12 4
1
2
3
4
5
6
7
8
700
800
900
1000
# 100
'''