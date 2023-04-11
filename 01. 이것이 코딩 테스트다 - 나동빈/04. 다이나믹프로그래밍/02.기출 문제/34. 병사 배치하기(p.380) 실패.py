# 34. 병사 배치하기(p.380)
# www.acmicpc.net/problem/18353
n = int(input())
array = list(map(int, input().split()))
result = 0

# for i in range(n-1):
#     if array[i] < array[i+1]:
#         result += 1
#
# if result == 0:
#     result = 1
d = [0] * (n+1)
d[0] = 1
x = 0

while x < n-1:

    temp = 0
    if array[x] > array[x+1]:
        d[x+1] = d[x] + 1
        x += 1
    elif array[x] < array[x+1]:

        for j in range(x+1, n-1):

            if array[j] < array[j+1]:
                x += 1
                temp += 1
                break
            elif array[j] > array[j+1]:
                x += 1
                temp += 1
                if j == n-2:
                    x += 1
                    temp += 1

                if array[j+1] < array[j-temp]:
                    break
            else:
                x += 1
            print(x, temp)
        print(1234)
        d[x] = max(d[x-temp], temp)

    else:
        d[x+1] = d[x]
        x += 1




print(d)
print(n - d[n-1])



