import numpy as np
m, n = map(int, input().split())
# m = key, n = lock m<=n
key = []
lock = []
for _ in range(m):
    key.append(list(map(int, input().split())))
for _ in range(n):
    lock.append(list(map(int, input().split())))

# for i in range(m):
#     print(key[i], end='\n')
# print('---------------------------')
# for i in range(n):
#     print(lock[i], end='\n')
# print('---------------------------')
# cnt = 0
cnt = 0
sum_lock= 0

checklist=[]
key_clone = np.array(key)
lock_clone = np.array(lock)
print(lock_clone)
m = len(key_clone[0])
n = len(lock_clone[0])



def rotation(key):
    rotated_key = list(map(list, zip(*key[::-1])))  # 시계방향 회전
    return rotated_key

def right(n,m):
    for t in range(n):
        for i in range(n):
            global cnt
            global sum_lock
            for k in range(m):
            #오른쪽으로 이동
                for j in range(m):
                    if j + i < n:
                        print(f'i = {i}, j = {j}, k = {k}, key[k][j] = {key[k][j]}, lock[k][j+i] = {lock_clone[k][j + i]} ')


                        if sum(lock[k]) < n:  # 가로줄에 0인부분이 있을때만 비교한다

                            if j + i < n:  # 오른쪽으로 이동하다가 넘어가는 부분은 비교하지 않는다.
                                #print(f'key[k][j] = {key[k][j]}, lock[k][j+k] = {lock[k][j + k]} ')

                                if key[k][j] == 1 and lock_clone[k+t][j+i] == 0:   # 열쇠가 들어갈 공간이 있으면
                                    cnt += 1
                                    #print(f'cnt = {cnt}')
            print(f'cnt = {cnt}')
            if cnt == count_zero:
                checklist.append(cnt)
                break
            cnt = 0

    return cnt

def down(n,m):
    for i in range(n):
        global cnt
        for k in range(m):

        #오른쪽으로 이동
            for j in range(m):
                if j + i < n:
                    print(f'i = {i}, j = {j}, k = {k}, key[k][j] = {key[k][j]}, lock[j+i][k] = {lock_clone[j+i][k]} ')
                    #if sum(lock[j+i][k]) < n:  # 가로줄에 0인부분이 있을때만 비교한다
                            #print(f'key[k][j] = {key[k][j]}, lock[k][j+k] = {lock[k][j + k]} ')
                    if key[k][j] == 1 and lock_clone[j+i][k] == 0:   # 열쇠가 들어갈 공간이 있으면
                        cnt += 1
                        print(f'cnt = {cnt}')
        #print(f'cnt = {cnt}')
        if cnt == n*n - sum_lock:
            checklist.append(cnt)
            break
        cnt = 0

    return cnt


# for i in range(n):
#
#     for j in range(4):
#         right(n,m)
#         rotation(key_clone)
#
#     if lock_clone.any():
#         lock_clone = np.delete(lock_clone, 0, axis=0)
#         n -= 1
#         if n == 0:
#             break
count_zero = lock_clone[np.where(lock_clone == 0)].size
# print(f'count_zero = {count_zero}')
lock_clone = np.delete(lock_clone, 0, axis=0)
# print(lock_clone)
# right(n,m)
# lock_clone = np.delete(lock_clone, 0, axis=0)
print('--------------')
right(n,m)
print(checklist)
if count_zero in checklist:
    answer = 'true'
else:
    answer = 'false'

print(answer)




            # if col_cnt == len(key[i]):
            #     col_cnt = 0



