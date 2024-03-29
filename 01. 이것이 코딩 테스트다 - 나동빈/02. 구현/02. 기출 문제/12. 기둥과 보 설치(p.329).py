def solution(n, build_frame):
    #map = [[0]*(n+1) for _ in range(n+1)]
    # ki = [1, 0]  #기둥
    # bo = [0, 1]  #보
    ki_list = []
    bo_list = []

    for i in range(len(build_frame)):
        x, y = build_frame[i][0], build_frame[i][1]
        #설치
        if build_frame[i][3] == 1:
            # 기둥일때
            if build_frame[i][2] == 0:
                if 0 <= x <= n and 0 <= y <= n-1:  # 맵을 벗어나지 않을 때만 설치
                    if y == 0 or [x - 1, y, 1] in bo_list or [x, y, 1] in bo_list or [x, y - 1, 0] in ki_list: # 바닥 or 보의 끝 or 기둥 위
                        ki_list.append([x, y, 0])
            #보일때
            else:
                if 0 <= x <= n-1 and 1 <= y <= n:
                    # 기둥위 or 양쪽끝에 보가 있음
                    if [x, y-1, 0] in ki_list or [x+1, y-1, 0] in ki_list or (
                            [x-1, y, 1] in bo_list and [x+1, y, 1] in bo_list):
                        bo_list.append([x, y, 1])


        #삭제
        else:
            #기둥일때
            if build_frame[i][2] == 0:   # ㅣ = 기둥 ￣ = 보
                #기둥 삭제 가능 할 때 :  i￣ㅣ or i￣ㅣ￣ ￣ or ㅣ￣ i or ￣ ￣ㅣ￣ i or ㅣ or ￣ ￣ㅣ￣ ￣ or ㅣ￣ㅣ￣ㅣ
                if ([x-1, y, 0] in ki_list and [x-1, y+1, 1] in bo_list and [x, y+1, 1] not in bo_list) or \
                        ([x-1, y, 0] in ki_list and [x-1, y+1, 1] in bo_list and [x, y+1, 1] in bo_list and [x+1, y+1, 1] in bo_list) or \
                        ([x+1, y, 0] in ki_list and [x, y+1, 1] in bo_list and [x-2, y+1, 1] in bo_list and [x-1, y+1, 1] in bo_list) or(
                        [x+1, y, 0] in ki_list and [x, y+1, 1] in bo_list and [x-1, y+1, 1] not in bo_list) or (
                        [x-1, y+1, 1] not in bo_list and [x, y+1, 1] not in bo_list and [x, y+1, 0] not in ki_list) or\
                        ([x-1, y, 0] in ki_list and [x-1, y+1, 1] in bo_list and [x, y+1, 1] in bo_list and [x+1, y+1, 1] in bo_list) or\
                        ([x-2, y+1, 1] in bo_list and [x-1, y+1, 1] in bo_list and [x, y+1, 1] in bo_list and [x+1, y+1, 1] in bo_list) or \
                        ([x-1, y, 0] in ki_list and [x-1, y+1, 1] in bo_list and [x, y+1, 1] in bo_list and [x+1, y, 0] in ki_list):

                    ki_list.remove([x, y, 0])
            else:
                #보 삭제 가능 할 때 : ㅣ￣  or ￣ㅣ or ㅣ￣ ￣ㅣ or ㅣ￣ ￣ㅣ or ㅣ￣  ￣  ￣ㅣ or ㅣ￣ㅣ
                if ([x, y-1, 0] in ki_list and [x+1, y, 0] not in ki_list and [x+1, y, 1] not in bo_list) or \
                        ([x+1, y-1, 0] in ki_list and ([x, y, 0] not in ki_list or [x-1, y, 1] not in bo_list)) or \
                        ([x, y-1, 0] in ki_list and [x+1, y, 1] in bo_list and [x+2, y-1, 0] in ki_list) or \
                        ([x+1, y-1, 0] in ki_list and [x-1, y, 1] in bo_list and [x-1, y-1, 0] in ki_list) or\
                        ([x-1, y-1, 0] in ki_list and [x-1, y, 1] in bo_list and [x+1, y, 1] in bo_list and [x+2, y-1, 0] in ki_list) or \
                        ([x, y-1, 0] in ki_list and [x+1, y-1, 0] in ki_list):

                    bo_list.remove([x, y, 1])

                # # 삭제 불가능일때 : 기둥을 삭제했는데 그 위치에 보만 떠있을 때 ( (￣ ㅣ일때 and ￣ ￣ ㅣ 아닐때) or (ㅣ￣ 일때 and ㅣ￣ ￣아닐때) or ( ㅣ ￣ ㅣ 아닐때 )
                # if ([x - 1, y + 1, 1] in bo_list and [x - 2, y + 1, 1] not in bo_list) or (
                #         [x, y + 1, 1] in bo_list and [x + 1, y + 1, 1] in bo_list):

    answer = ki_list + bo_list
    answer.sort()
    print(answer)
    return answer




# Input

N1 = 5
BUILD_FRAME1 = [[1, 0, 0, 1],
                [1, 1, 1, 1],
                [2, 1, 0, 1],
                [2, 2, 1, 1],
                [5, 0, 0, 1],
                [5, 1, 0, 1],
                [4, 2, 1, 1],
                [3, 2, 1, 1]]

N2 = 5
BUILD_FRAME2 = [[0, 0, 0, 1],
                [2, 0, 0, 1],
                [4, 0, 0, 1],
                [0, 1, 1, 1],
                [1, 1, 1, 1],
                [2, 1, 1, 1],
                [3, 1, 1, 1],
                [2, 0, 0, 0],
                [1, 1, 1, 0],
                [2, 2, 0, 1]]

N3 = 100
BUILD_FRAME3 = [[2, 0, 0, 1],
                [100, 0, 0, 1],
                [100, 1, 1, 1],
                [99, 1, 1, 1],
                [99, 1, 0, 1],
                [99, 0, 0, 1]]
result = [[2, 0, 0], [99, 0, 0], [99, 1, 0], [99, 1, 1], [100, 0, 0]]

N4 = 5
BUILD_FRAME4 = [[0, 0, 0, 1],
                [1, 0, 1, 1],
                [2, 0, 1, 1],
                [3, 0, 1, 1],
                [4, 0, 1, 1],
                [5, 0, 1, 1]]

N5 = 5
BUILD_FRAME5 = \
      [[0, 0, 0, 1],
      [1, 0, 0, 1],
      [1, 1, 0, 1],
      [0, 1, 1, 1],
      [1, 2, 1, 1],
      [2, 2, 0, 1],
      [2, 3, 1, 1],
      [3, 0, 0, 1],
      [2, 1, 1, 1],
      [3, 1, 0, 1],
      [2, 2, 1, 1],
      [3, 1, 1, 1],
      [4, 1, 0, 1],
      [4, 2, 1, 1],
      [5, 0, 0, 1],
      [5, 2, 0, 1],
      [0, 1, 1, 0],
      [1, 1, 0, 0],
      [1, 2, 1, 0],
      [2, 2, 0, 0],
      [2, 3, 1, 0],
      [3, 0, 0, 0],
      [2, 1, 1, 0],
      [4, 1, 0, 0],
      [5, 0, 0, 0],
      [4, 2, 1, 0],
      [5, 2, 0, 0]]

result = [[0, 0, 0],[1, 0, 0],[1, 1, 0],[1, 2, 1],[2, 2, 0], [2, 2, 1],[3, 0, 0],[3, 1, 0],[3, 1, 1],[4, 1, 0],[4, 2, 1]]
# Output
solution(N1, BUILD_FRAME1)