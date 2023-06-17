n = int(input())
array = list(map(int, input().split()))

def BTS(array, start, end):
    mid = (start + end) // 2
    if start > end:
        return -1
    if array[mid] == mid:
        return mid
    elif array[mid] < mid:
        return BTS(array, mid + 1, end)
    else:
        return BTS(array, start, mid - 1)
    return

start = 0
end = len(array) - 1
print(BTS(array, start, end))

# 5
# -15 -6 1 3 7
# res = 3

# 7
# -15 -4 2 8 9 13 15
# res = 2

# 7
# -15 -4 3 8 9 13 15
# res = -1