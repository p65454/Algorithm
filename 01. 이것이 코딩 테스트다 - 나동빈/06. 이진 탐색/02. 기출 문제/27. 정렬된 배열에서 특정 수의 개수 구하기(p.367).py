n, x = map(int, input().split())
array = list(map(int, input().split()))

start = 0
end = len(array) - 1

def count_x(array, index, target):
    cnt_x = 0
    temp = index + 1
    while array[index] == target:
        cnt_x += 1
        if 0 < index <= end:
            index -= 1
        else:
            break
    while array[temp] == target:
        cnt_x += 1
        if 0 <= temp < end:
            temp += 1
        else:
            break
    return cnt_x

def answer(array, start, end):
    while(start <= end):
        mid = (start + end) // 2
        if array[mid] == x:
            return count_x(array, mid, x)
        elif array[mid] < x:
            start = mid + 1
        else:
            end = mid - 1
    return -1

print(answer(array, start, end))

# 7 2
# 1 1 2 2 2 2 3
# res = 4

# 7 4
# 1 1 2 2 2 2 3
# res = -1

# 9 5
# 1 1 2 2 3 3 4 4 5
# res = 1

# 6 2
# 2 2 2 2 2 2
# res = 6



