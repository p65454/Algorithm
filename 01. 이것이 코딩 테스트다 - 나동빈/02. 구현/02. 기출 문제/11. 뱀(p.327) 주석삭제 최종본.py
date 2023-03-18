# 11.뱀(p.327)
# https://www.acmicpc.net/problem/3190
apple = []
snake_direction = []
n = int(input())
k = int(input())
for _ in range(k):
    apple.append(list(map(int, input().split())))
L = int(input())
for i in range(L):
    snake_direction.append(list(map(str, input().split())))
    snake_direction[i][0] = int(snake_direction[i][0])

#보드 생성
board = [[0]*n for _ in range(n)]
for i in range(len(apple)): # 사과의 위치는 -1로 표기
    board[apple[i][0]-1][apple[i][1]-1] += -1

#방향설정 (동, 남, 서, 북)
cnt = 0
dir = 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
x, y = 0, 0     # 뱀의 좌표 ( 뱀:1 , 사과:-1, 아무것도없다:0 )
board[x][y] = 1 # 뱀의 초기 머리위치 1
d = 0   # 방향 정할때(동서남북) 사용

direction_data = []
snake = [[x, y]]
# 뱀의 방향정보 넣어주기
for i in range(len(snake_direction)):
    direction_data.append(snake_direction[i][1])

while True:
    snake_x = x + dx[dir]
    snake_y = y + dy[dir]
    # 1. 먼저 뱀은 몸길이를 늘려 머리를 다음 칸에 위치시킵니다.
    # 1-1 뱀이 벽에 부딪히지 않았으면서, 자신의 몸에 부딪히지도 않았을 때
    if snake_x >= 0 and snake_x < n and snake_y >= 0 and snake_y < n and board[snake_x][snake_y] != 1:
        # 2. 만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않습니다.
        # 2-1 만약 사과가 있다면, 사과대신 뱀머리로 채운다
        if board[snake_x][snake_y] == -1:
            board[snake_x][snake_y] = 1
            snake.append([snake_x, snake_y])#뱀의 머리가 이동한 좌표 추가

        # 2-2 만약 사과가 없다면, 뱀머리 이동 후에 꼬리 제거
        if board[snake_x][snake_y] == 0:
            board[snake_x][snake_y] = 1
            snake.append([snake_x, snake_y]) #뱀 좌표추가
            a = snake.pop(0)                 #꼬리 제거
            # 3. 만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워줍니다. 즉, 몸길이는 변하지 않습니다.
            board[a[0]][a[1]] = 0            #꼬리 제거한 곳 다시 비우기
    # 벽에 부딪히거나, 자신의 몸에 부딪혔을 때
    else:
        cnt += 1
        break

    x, y = snake_x, snake_y  # 움직인 좌표 바꿔주기
    cnt += 1

    # 뱀이 이동경로를 바꿀 시간이 됐을 때
    if cnt == snake_direction[d][0]:
        if direction_data[d] == 'D':  # 방향이 오른쪽일 때(D)
            if dir == 3:
                dir = 0
            else:
                dir += 1
        else:                         # 방향이 왼쪽일 때(L)
            if dir == 0:
                dir = 3
            else:
                dir -= 1

        if d < len(snake_direction)-1: # index 에러 나지 않도록 범위 설정
            d += 1
print(cnt)
# 6
# 3
# 3 4
# 2 5
# 5 3
# 3
# 3 D
# 15 L
# 17 D