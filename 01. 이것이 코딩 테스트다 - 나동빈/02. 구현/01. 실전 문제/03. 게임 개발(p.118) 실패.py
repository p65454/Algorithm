n, m = map(int, input().split())   # n = 세로, m = 가로
a, b, d = map(int, input().split())  # a,b = 처음위치 좌표 / d=바라보는방향 - 0:북, 1:동, 2:남, 3:서
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

# print(n,m)
# print(a,b,d)
# print(board)

#man_pos = board[a][b]
result = 0
#print(man_pos)
cur_pos = [(a,b)]
check = []
while True:
    print(result)
    while len(d)<4:

    #cur_pos=[]
    # cur_pos.append(a)
    # cur_pos.append(b)
    # print(cur_pos)

    # 현재방향 기준 반시계 방향을 바라본다(case1)
    # if d == 0:
    #     d = 3
    # else:
    #     d -= 1

        if d == 0:    # 서쪽을 바라본다
            if board[a][b-1] == 0 and ((a, b-1) not in cur_pos):  # 육지일때, 그리고 가보지 않은 칸일때
                b -= 1     # 서쪽으로 이동
                result += 1
                d = 3

                cur_pos.append((a,b))
                print(b,result)
            else:       #이미 가본 칸이거나 바다로 되어있을 경우 (case3)
                # 방향 원상복구 한 상태로 뒤로 1칸 이동
                d = 3
                check.append(d)

                # if board[a+1][b] == 0: # 뒤로1칸 이동할 곳이 육지라면
                #     a += 1
                #     if (a+1, b) not in cur_pos:  # 안가본곳이면
                #         result += 1
                #         cur_pos.append((a+1, b))
                # else:                 # 뒤로1칸 이동할 곳이 바다라면
                #     break

        elif d == 3:  # 남쪽을 바라본다
            if board[a+1][b] == 0 and (a+1, b) not in cur_pos:  # 육지일때, 그리고 가보지 않은 칸일때
                a += 1     # 남쪽으로 이동
                result += 1
                d -= 1
                cur_pos.append((a, b))
            else:       #이미 가본 칸이거나 바다로 되어있을 경우 (case3)
                # 방향 원상복구 한 상태로 뒤로 1칸 이동
                d -= 1
                check.append(d)

                # if board[a][b+1] == 0: # 뒤로1칸 이동할 곳이 육지라면
                #     b += 1
                #     if (a, b+1) not in cur_pos:
                #         result += 1
                #         cur_pos.append((a, b+1))
                # else:                 # 뒤로1칸 이동할 곳이 바다라면
                #     break

        elif d == 2:  # 동쪽을 바라본다
            if board[a][b+1] == 0 and (a, b+1) not in cur_pos:  # 육지일때, 그리고 가보지 않은 칸일때
                b += 1     # 동쪽으로 이동
                result += 1
                d -= 1
                cur_pos.append((a, b))
            else:       #이미 가본 칸이거나 바다로 되어있을 경우 (case3)
                # 방향 원상복구 한 상태로 뒤로 1칸 이동
                d -= 1
                check.append(d)

                # if board[a-1][b] == 0: # 뒤로1칸 이동할 곳이 육지라면
                #     a -= 1
                #     if (a-1, b) not in cur_pos:
                #         result += 1
                #         cur_pos.append((a-1, b))
                # else:                 # 뒤로1칸 이동할 곳이 바다라면
                #     break

        elif d == 1: # 북쪽을 바라본다
            if board[a-1][b] == 0 and (a-1, b) not in cur_pos:  # 육지일때, 그리고 가보지 않은 칸일때
                a -= 1     # 북쪽으로 이동
                result += 1
                d -= 1
                cur_pos.append((a, b))
            else:       #이미 가본 칸이거나 바다로 되어있을 경우 (case3)
                # 방향 원상복구 한 상태로 뒤로 1칸 이동
                d -= 1
                check.append(d)



                # if board[a][b-1] == 0: # 뒤로1칸 이동할 곳이 육지라면
                #     b -= 1
                #     if (a, b-1) not in cur_pos:
                #         result += 1
                #         cur_pos.append((a, b-1))
                # else:                 # 뒤로1칸 이동할 곳이 바다라면
                #     break

print(result)





