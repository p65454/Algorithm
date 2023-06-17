n, x = map(int, input().split())
array = list(map(int, input().split()))

start = 0
end = len(array) - 1
cnt = 0
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



