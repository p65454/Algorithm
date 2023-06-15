n = int(input())
array1 = list(map(int, input().split()))
m = int(input())
array2 = list(map(int, input().split()))
array1.sort()
array2.sort()
#print(n,m,array1, array2)
result = []
def binary_search(array, target, start, end):
    if start > end:
        result.append('no')
        return result
    mid = (start + end) // 2
    if array[mid] == target:
        result.append('yes')
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)
    return result

for i in range(m):
    binary_search(array1, array2[i], 0, n-1)

print(' '.join(result))
#print(binary_search(array1, 4, 0, n-1))


'''
5
8 3 7 9 2
3
5 7 9
# no yes yes

5
8 3 7 9 2
3
1 4 5
# no no no
'''
