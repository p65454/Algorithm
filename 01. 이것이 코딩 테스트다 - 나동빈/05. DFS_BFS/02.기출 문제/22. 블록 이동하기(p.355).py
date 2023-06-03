# https://school.programmers.co.kr/learn/courses/30/lessons/60063
from collections import deque
def solution(board):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    n = len(board)
    robot = {(0, 0), (0, 1)}
    q = deque()
    for i in range(4):



    answer = 0
    return answer


board = [[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]
print(len(board))
n = len(board)

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
