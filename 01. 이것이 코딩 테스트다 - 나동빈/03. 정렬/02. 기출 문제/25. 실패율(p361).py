# 25. 실패율(p.361)
# https://school.programmers.co.kr/learn/courses/30/lessons/42889

def solution(N, stages):
    stages.sort()
    fail_list = []
    fail = 0
    num = 0
    cnt = len(stages)
    while cnt != 0:
        cnt = len(stages)

        if stages[0] <= N:
            num = stages.count(stages[0])
            fail = num / cnt
            fail_list.append((stages[0], fail))
            for _ in range(num):
                stages.pop(0)
            cnt -= num
        else:
            stages.pop(0)
            cnt -= 1

    answer_list = []
    fail_list.sort(key = lambda x : (-x[1], x[0]))
    for i in range(len(fail_list)):
        answer_list.append(fail_list[i][0])

    for i in range(1,N+1):
        if i not in answer_list:
            answer_list.append(i)

    return answer_list



N = 5
stages = [2,1,2,6,2,4,3,3]
#stages = [4,4,4,4,4,4]
result = [3,4,2,1,5]

print(solution(N, stages)




