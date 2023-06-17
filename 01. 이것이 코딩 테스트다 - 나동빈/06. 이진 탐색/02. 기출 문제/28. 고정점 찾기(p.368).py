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
