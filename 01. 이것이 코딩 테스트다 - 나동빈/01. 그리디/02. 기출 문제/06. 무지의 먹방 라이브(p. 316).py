def solution(food_times, k):
    result = 0
    cnt = 0
    n = []
    while sum(food_times) != 0 and cnt < k + 1:
        for i in range(len(food_times)):

            if food_times[i] > 0:
                if cnt < k + 1:
                    food_times[i] -= 1
                    cnt += 1

                if cnt == k + 1:  # 네트워크 장애 발생했을 때
                    food_times[i] += 1
                    result = i + 1
                    break

            if sum(food_times) == 0:
                result = -1
                break
    return result