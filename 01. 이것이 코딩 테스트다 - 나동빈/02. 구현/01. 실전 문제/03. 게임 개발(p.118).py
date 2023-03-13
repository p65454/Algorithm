n, m = map(int, input().split())   # n = 세로, m = 가로
a, b, d = map(int, input().split())  # a,b = 처음위치 좌표 / d=바라보는방향 - 0:북, 1:동, 2:남, 3:서
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

result = 1
move = [(-1, 0), (0, -1), (1, 0), (0, 1)]  # 리스트의 0:북쪽, 3:서쪽, 2:남쪽, 1:동쪽
cur_pos = [(a,b)]
memory = d


check = 0
next_pos = board[a+move[d][0]][b+move[d][1]]
#현재 방향부터 반시계 방향으로 돌아가면서 움직 일 수 있는지 체크
while True:
    for _ in range(4):
        print(a,b,result,cur_pos)
        if d == 0:
            d = 3
        else:
            d -= 1

        if (next_pos == 0) and (next_pos not in cur_pos):  #해당 방향의 다음 칸이 육지이면서, 가보지 않은 칸일 때
            a += move[d][0]
            b += move[d][1]
            result += 1
            cur_pos.append((a, b))
            break
        else:                                               #갈 수 없을 때
            check += 1

    if check == 4:   # 네 방향 다 갈 수 없을 때
        if board[a-move[d][0]][b-move[d][1]] == 0:   # 뒤로 갈 곳이 육지라면
            a -= move[d][0]
            b -= move[d][1]
            if (a, b) not in cur_pos:                #
                cur_pos.append((a, b))
                result += 1
        else:
            break
print(result)


