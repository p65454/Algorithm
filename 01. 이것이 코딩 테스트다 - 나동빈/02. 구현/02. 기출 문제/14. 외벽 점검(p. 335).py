#14.외벽 점검(p. 335)
#https://school.programmers.co.kr/learn/courses/30/lessons/60062#

# weak 각각의 차 리스트 만든다
# 가장 앞에 있는 최대값 찾아서 제외.
# 최대값 양옆의 인덱스 기억 (반드시 점검해야 할 부분),  sum = n - 최대값
# 양옆의 인덱스 요소를 제외한 나머지 값들 중에서 최대값 찾는다. ( 다시 최대값 양옆 찾고 체크)
# 최대값 2개의 양 옆의 요소들 을 다시 정렬
# ex) n=15,  [1, 2, 3, 7, 11, 12, 13]  ->  [1, 1, 4, 4, 1, 1, 3]
# ex) [[1,1], [4,1,1]] 이라면 [2,6] 이므로 dist에서 6이상이 있는지 확인
# 없다면 result
#
def solution(n, weak, dist):
    # weak 각각의 차 리스트 만든다
    memory = []
    sub_weak = []
    for i in range(len(weak) - 1):
        sub_weak.append(weak[i+1] - weak[i])
    sub_weak.append(n - weak[-1] + weak[0])
    print(sub_weak)

    # 가장 앞에 있는 최대값 찾아서 제외.
    max1 = 0
    temp = 0
    for i in range(len(sub_weak)):
        temp = sub_weak[i]
        if temp > max1:
            max1 = temp

    #print(type(sub_weak))
    #print(max(sub_weak))

    # 최대값 양옆의 인덱스 기억 (반드시 점검해야 할 부분),  sum = n - 최대값
    print(sub_weak.index(max(sub_weak)))
    max_index = sub_weak.index(max(sub_weak))

    if max_index + 1 == len(sub_weak):
        right_index = 0
        left_index = max_index - 1
    elif max_index == 0:
        right_index = max_index + 1
        left_index = len(sub_weak) - 1
    else:
        right_index = max_index + 1
        left_index = max_index - 1
    # 양옆의 인덱스 요소를 제외한 나머지 값들 중에서 최대값 찾는다. ( 다시 최대값 양옆 찾고 체크)
    new_subweak = []
    # remove_list.append(sub_weak[max_index])
    # remove_list.append(sub_weak[right_index])
    # remove_list.append(sub_weak[left_index])
    # new_subweak = [i for i in sub_weak if i not in remove_list]
    #print(new_subweak)
    #new_subweak.append(sub_weak[left_index])

    del sub_weak[left_index, max_index, right_index]
    print(sub_weak)








    answer = 0
    return answer


#input
# n = 12
# weak = [1, 5, 6, 10]
# dist = [1, 2, 3, 4]
# Result = 2
n = 15
weak = [1,2,3,7,8,11,12,13]
dist = [1,2,3,4,5]
result = 3

solution(n,weak,dist)
