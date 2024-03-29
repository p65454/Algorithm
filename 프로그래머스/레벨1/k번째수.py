def solution(array, commands):
    '''
    https://school.programmers.co.kr/learn/courses/30/lessons/42748
    
    풀이1)
    문제대로 슬라이싱 한 다음에 sort 하고 k번째 담아서 return 하면 될거같다
    
    예시)    
    array = [1, 5, 2, 6, 3, 7, 4]
    commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
    return = [5, 6, 3]
    '''
    answer = []    
    for com in commands: 
        i = com[0]
        j = com[1]
        k = com[2]
        temp = array[i-1:j]      
        temp.sort()
        answer.append(temp[k-1])
    
    return answer