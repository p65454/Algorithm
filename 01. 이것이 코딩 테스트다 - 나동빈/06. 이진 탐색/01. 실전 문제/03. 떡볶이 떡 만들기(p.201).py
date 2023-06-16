import sys, time
# start = time.time()
n, m = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))
array.sort()
result = []
def BTS(array, start, end):
    request = 0
    height = (start + end) // 2
    if start > end:
        return
    for i in range(len(array)):
        if array[i] > height:
            request += array[i] - height
    if request < m:
        return BTS(array, start, height - 1)
    else:
        result.append((request, height))
        return BTS(array, height + 1, end)

BTS(array, 0, array[-1])
result.sort()
print(result[0][1])

# end = time.time()
# print(start)
# print(end)
# print(f"{end - start:.5f} sec")


