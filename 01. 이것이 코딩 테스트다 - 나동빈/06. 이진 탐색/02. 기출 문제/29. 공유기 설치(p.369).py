# https://www.acmicpc.net/problem/2110
n, c = map(int, input().split())
array = []
for _ in range(n):
    x = int(input())
    array.append(x)
array.sort()
print(array)

distance_wifi = []
def BTS(array, start, end):
    cnt = c - 2
    mid = (start + end) // 2
    while(start != mid and mid != end and cnt > 0):
        print(distance_wifi, cnt)
        left = array[mid] - array[start]
        right = array[end] - array[mid]
        distance_wifi.append(left)
        distance_wifi.append(right)
        if left > right:
            end = mid
            mid = (start + end) // 2
        else:
            start = mid
            mid = (start + end) // 2
        cnt -= 1

    return distance_wifi
print(BTS(array, 0, n-1))
result = BTS(array, 0, n-1)
result.sort()
print(result[0])