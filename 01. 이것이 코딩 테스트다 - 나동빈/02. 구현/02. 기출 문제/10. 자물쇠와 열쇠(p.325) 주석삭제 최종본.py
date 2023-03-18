# 10. 자물쇠와 열쇠 (p. 325)
# https://programmers.co.kr/learn/courses/30/lessons/60059

def rotation(key):
    rotated_key = list(map(list, zip(*key[::-1])))  # 시계방향 회전
    return rotated_key

def solution(key, lock):
    n = len(lock)
    m = len(key)
    cnt = 0
    new_lock = [[0] * (n * 3) for _ in range(n * 3)]
    # 자물쇠 3배크기로 키우기
    for i in range(n):
        for j in range(n):
            new_lock[i + n][j + n] = lock[i][j]

    for _ in range(4):
        key = rotation(key)
    # 자물쇠 + 키  해서 모든 자물쇠의 합이 1이면 True
        for a in range(n-m+1, 2*n):
            for b in range(n-m+1, 2*n):
                for i in range(m):
                    for j in range(m):
                        new_lock[a+i][b+j] += key[i][j]

                #키가 자물쇠랑 맞는지 검사
                for c in range(n, 2*n):
                    for d in range(n, 2*n):
                        if new_lock[c][d] == 1:
                            cnt += 1

                if cnt == n*n:
                    return True
                cnt = 0
                #위에서 True가 안됐을시 키가 안맞는거니까 다시 빼줌
                for i in range(m):
                    for j in range(m):
                        new_lock[a+i][b+j] -= key[i][j]

    return False

## Input
key = [[0, 1],
       [1, 0]]
lock = [[1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 0, 1, 1],
        [0, 1, 1, 1]]

# Output
print(solution(key, lock))