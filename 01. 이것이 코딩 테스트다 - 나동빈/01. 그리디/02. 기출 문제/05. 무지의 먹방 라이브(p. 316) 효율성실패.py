def solution(food_times,k):
    result = 0
    # for i in range(max(food_times)):
    #     circle = list(map(lambda x: x>i, food_times))
    #     print(len(circle),k,i,result)
    #
    #     if k >= len(circle):
    #         k -= len(circle)
    #
    #     else:
    #         result = circle.index(i)
    L = len(food_times)
    m = 0
    cnt = 0

    def findmin(food, min_value):
        temp1 = 0
        temp2 = 0
        global cnt

        for i in range(L):      # [1,1,1,4,5] - [0,0,0,4,5]

            if food[i] == min_value:
                food[i] = 0
            if food[i] > 0:
                if temp1 == 0:
                    temp1 = food[i]
                else:
                    temp2 = food[i]
                    if temp1 > temp2:
                        temp1 = temp2
        cnt = food.count(temp1)

        return temp1


    while True:
        previous = m
        m = findmin(food_times, previous)
        if k >= (m-previous)*(L-cnt):   # k -= (다음최소값-이전최소값) x (L - 이전최소값의 개수)
            k -= (m-previous)*(L-cnt)
        else:
            k






    return result
print(solution([3,1,3,6,8],7))