# https://school.programmers.co.kr/learn/courses/30/lessons/60063
from collections import deque
def solution(board):
    global n
    n = len(board)
    robot = {(0, 0), (0, 1)}
    q = deque()
    visit = []
    q.append((robot, 0))
    while q:
        point, time = q.popleft()
        if (n-1, n-1) in point:
            return time
        for move_point in move(point, board, n):
            if move_point not in visit:
                q.append((move_point, time+1))
                visit.append(move_point)

        for rotation_point in rotation(point, board, n):
            if rotation_point not in visit:
                q.append((rotation_point, time+1))
                visit.append(rotation_point)

    return


def move(robot, board, n):
    point = []
    robot_list = list(robot)
    dx = [0, 0, 1, -1]    # 우 좌 하 상
    dy = [1, -1, 0, 0]
    for i in range(4):
        x1, y1 = robot_list[0][0], robot_list[0][1]
        x2, y2 = robot_list[1][0], robot_list[1][1]
        nx1, ny1 = x1 + dx[i], y1 + dy[i]
        nx2, ny2 = x2 + dx[i], y2 + dy[i]
        if 0 <= nx1 < n and 0 <= nx2 < n and 0 <= ny1 < n and 0 <= ny2 < n and board[nx1][ny1] == 0 and board[nx2][ny2] == 0:
            point.append({(nx1, ny1), (nx2, ny2)})

    return point
def rotation(robot, board, n):
    point = []
    robot_list = list(robot)
    x1, y1 = robot_list[0][0], robot_list[0][1]
    x2, y2 = robot_list[1][0], robot_list[1][1]
    if robot_list[0][0] == robot_list[1][0]:  # 로봇이 가로로 있는 경우
        if x1 + 1 < n and board[x1 + 1][y1] == 0 and board[x2 + 1][y2] == 0:  # 아래로 90도 회전
            point.append({(x1 + 1, y1), (x1, y1)})
            point.append({(x2, y2), (x2 + 1, y2)})
        if x1 - 1 >= 0 and board[x1 - 1][y1] == 0 and board[x2 - 1][y2] == 0:  # 위로 90도 회전
            point.append({(x1 - 1, y1), (x1, y1)})
            point.append({(x2 - 1, y2), (x2, y2)})

    else:  # 로봇이 세로로 있는 경우
        if y1 + 1 < n and board[x1][y1 + 1] == 0 and board[x2][y2 + 1] == 0:  #  오른쪽으로 90도 회전
            point.append({(x1, y1 + 1), (x1, y1)})
            point.append({(x2, y2), (x2, y2 + 1)})
        if y1 - 1 >= 0 and board[x1][y1 - 1] == 0 and board[x2][y2 - 1] == 0:  # 왼쪽으로 90도 회전
            point.append({(x1, y1 - 1), (x1, y1)})
            point.append({(x2, y2), (x2, y2 - 1)})

    return point


board = [[0, 0, 1, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]
#7

board1 = [[0, 0, 0, 0, 0, 0, 1],
          [1, 1, 1, 1, 0, 0, 1],
          [0, 0, 0, 0, 0, 0, 0],
          [0, 0, 1, 1, 1, 0, 0],
          [0, 1, 1, 1, 1, 1, 0],
          [0, 0, 0, 0, 0, 1, 0],
          [0, 0, 1, 0, 0, 0, 0]]
#

board2 = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
          [1, 1, 1, 1, 1, 1, 1, 0, 0],
          [1, 1, 1, 1, 1, 1, 1, 1, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 1, 1, 1, 1, 1, 0, 0],
          [0, 1, 1, 1, 1, 1, 1, 1, 1],
          [0, 0, 1, 1, 1, 1, 1, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [1, 1, 1, 1, 1, 1, 1, 1, 0]]
#33


# board = [[0, 0, 1, 0, 0, 0],
#          [0, 0, 1, 0, 0, 0],
#          [0, 1, 0, 0, 0, 0],
#          [0, 0, 0, 0, 1, 0],
#          [0, 0, 0, 1, 0, 0],
#          [0, 0, 1, 1, 0, 0]]
#print(len(board))
#n = len(board)
print(solution(board2))