def solution(n, build_frame):
    ki_list = []
    bo_list = []
    for i in range(len(build_frame)):
        x, y = build_frame[i][0], build_frame[i][1]
        #설치
        if build_frame[i][3] == 1:
            # 기둥일때
            if build_frame[i][2] == 0:
                if 0 <= x <= n+1 and 0 <= y <= n:  # 맵을 벗어나지 않을 때만 설치
                    if y == 0 or [x - 1, y, 1] in bo_list or [x, y, 1] in bo_list or [x, y - 1, 0] in ki_list: # 바닥 or 보의 끝 or 기둥 위
                        ki_list.append([x, y, 0])
            #보일때
            else:
                if 0 <= x <= n+1 and 1 <= y <= n+1:
                    # 기둥위 or 양쪽끝에 보가 있음
                    if [x, y-1, 0] in ki_list or [x+1, y-1, 0] in ki_list or (
                            [x-1, y, 1] in bo_list and [x+1, y, 1] in bo_list):
                        bo_list.append([x, y, 1])
        #삭제
        else:
            if build_frame[i][3] == 0:
                #기둥일때
                if build_frame[i][2] == 0:  # ㅣ = 기둥 ￣ = 보
                    # 기둥 삭제 가능 할 때 :  i￣ㅣ or ㅣ￣ i or ㅣ or ￣ ￣ㅣ￣ ￣
                    if ([x - 1, y, 0] in ki_list and [x - 1, y + 1, 1] in bo_list and [x, y + 1, 1] not in bo_list) or
                            ([x + 1, y, 0] in ki_list and [x, y + 1, 1] in bo_list and [x - 1, y + 1, 1] not in bo_list) or (
                            [x - 1, y + 1, 1] not in bo_list and [x, y + 1, 1] not in bo_list and [x, y 1, 0] not in ki_list) or (
                            [x - 2, y + 1, 1] in bo_list and [x - 1, y + 1, 1] in bo_list and [x, y + 1, 1] in bo_list and [x + 1, y + 1, 1] in bo_list):
                        ki_list.remove([x, y, 0])

                else:
                    #보 삭제 가능 할 때 : ㅣ￣ or ￣ㅣ or  ㅣ￣  ￣  ￣ㅣ
                    if [x, y-1, 0] in ki_list or [x+1, y-1, 0] in ki_list or (
                            [x-1, y-1, 0] in ki_list and [x-1, y, 1] in bo_list and
                            [x+1, y, 1] in bo_list and [x+1, y-1, 0] in ki_list):
                        bo_list.remove([x, y, 1])

    answer = ki_list + bo_list
    answer.sort()
    return answer