#자물쇠를 3배로 키운다


def rotation(key):
    rotated_key = list(map(list, zip(*key[::-1])))  # 시계방향 회전
    return rotated_key

# def right(new_lock):
#     length = len(new_lock) // 3
#     for a in range(length,):
#     return

key = [[0, 1],
       [1, 0]]
lock = [[1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 0, 1, 1],
        [0, 1, 1, 1]]

def solution(key, lock):
    n = len(lock)
    m = len(key)
    cnt = 0
    new_lock = [[0] * (n * 3) for _ in range(n * 3)]

    # print(new_lock)

    # 자물쇠 3배크기로 키우기
    for i in range(n):
        for j in range(n):
            new_lock[i + n][j + n] = lock[i][j]

    # for i in range(n * 3):
    #     print(new_lock[i], end='\n')

    for _ in range(4):
        key = rotation(key)
    # 자물쇠 + 키  해서 모든 자물쇠의 합이 1이면 True
        for a in range(n-m+1,2*n):
            for b in range(n-m+1,2*n):
                print(f'a = {a}, b = {b}')
                for i in range(m):
                    for j in range(m):
                        new_lock[a+i][b+j] += key[i][j]

                #키가 자물쇠랑 맞는지 검사
                for c in range(n, 2*n):
                    for d in range(n, 2*n):
                        if new_lock[c][d] == 1:
                            cnt += 1
                print(f'cnt = {cnt}')
                for i in range(n * 3):
                    print(new_lock[i], end='\n')
                print('---------------------------------')
                if cnt == n*n:
                    return True
                cnt = 0

                #위에서 True가 안됐을시 키가 안맞는거니까 다시 빼줌
                for i in range(m):
                    for j in range(m):
                        new_lock[a+i][b+j] -= key[i][j]



        #자물쇠
        for i in range(n * 3):
            print(new_lock[i], end='\n')

    return False


# def right(n,m):
#     for t in range(n):
#         for i in range(n):
#             global cnt
#             global sum_lock
#             for k in range(m):
#             #오른쪽으로 이동
#                 for j in range(m):
#                     if j + i < n:
#                         print(f'i = {i}, j = {j}, k = {k}, key[k][j] = {key[k][j]}, lock[k][j+i] = {lock_clone[k][j + i]} ')
#
#
#                         if sum(lock[k]) < n:  # 가로줄에 0인부분이 있을때만 비교한다
#
#                             if j + i < n:  # 오른쪽으로 이동하다가 넘어가는 부분은 비교하지 않는다.
#                                 #print(f'key[k][j] = {key[k][j]}, lock[k][j+k] = {lock[k][j + k]} ')
#
#                                 if key[k][j] == 1 and lock_clone[k+t][j+i] == 0:   # 열쇠가 들어갈 공간이 있으면
#                                     cnt += 1
#                                     #print(f'cnt = {cnt}')
#             print(f'cnt = {cnt}')
#             if cnt == count_zero:
#                 checklist.append(cnt)
#                 break
#             cnt = 0
#
#     return cnt

print(solution(key,lock))
# 0 1
# 1 0
# 1 1 1 1
# 1 1 1 1
# 1 0 1 1
# 0 1 1 1