# https://school.programmers.co.kr/learn/courses/30/lessons/118667

# 1. deque를 활용한 풀이

from collections import deque
def solution(queue1, queue2):
    total = sum(queue1) + sum(queue2) 
    n = len(queue1)
    q1_sum = sum(queue1)
    q2_sum = sum(queue2)
    q1 = deque(queue1)
    q2 = deque(queue2)
    
    if total % 2 == 1:
        return -1                            
        
    for i in range(4 * n):
        if q1_sum == q2_sum:
            return i
        if q1_sum > q2_sum : 
            num = q1.popleft()
            q1_sum -= num
            
            q2.append(num)
            q2_sum += num
        else:
            num = q2.popleft()
            q2_sum -= num
            
            q1.append(num)
            q1_sum += num       
         
    return -1

# 2. two pointer 풀이 (시간복잡도 더 낮았음)

def solution(queue1, queue2):
    total_q = queue1 + queue2
    if sum(total_q) % 2 == 1:
        return -1
    q1_start, q2_start = 0, len(total_q) // 2
    ans = 0
    
    q1_sum = sum(total_q[q1_start:q2_start])
    q2_sum = sum(total_q[q2_start:])
    total_len = len(total_q)
    
    while q1_start < total_len and q2_start < total_len:
        if q1_sum < q2_sum:
            dequeue_value = total_q[q2_start]
            q2_sum -= dequeue_value
            q1_sum += dequeue_value
            q2_start += 1
            
        elif q1_sum > q2_sum:
            dequeue_value = total_q[q1_start]
            q1_sum -= dequeue_value
            q2_sum += dequeue_value
            q1_start += 1
            
        else:
            return ans
        ans += 1
        
    return -1