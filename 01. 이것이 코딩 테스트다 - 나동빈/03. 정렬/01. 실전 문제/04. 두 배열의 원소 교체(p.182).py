n, k = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)
print(A)
print(B)
for i in range(k):
    if A[i] < B[i]:
        A[i], B[i] = B[i], A[i]
    else:
        break
print(A)
print(sum(A))