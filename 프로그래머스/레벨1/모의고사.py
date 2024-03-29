def solution(answers):
    '''
    풀이1)
    for문 돌려서 조건식 때려박으면 되지않을까?
    근데 이렇게 쉬울까? 뭔가 이상한데 일단해보자
    
    풀이2)
    
    
    
    
    '''
    array1 = [1,2,3,4,5]
    array2 = [2,1,2,3,2,4,2,5]
    array3 = [3,3,1,1,2,2,4,4,5,5]
    
    n1 = len(array1)
    n2 = len(array2)
    n3 = len(array3)
    
    r1 = 0
    r2 = 0
    r3 = 0
    
    for i in range(len(answers)):
        if answers[i] == array1[i % n1]:
            r1 += 1
        if answers[i] == array2[i % n2]:
            r2 += 1
        if answers[i] == array3[i % n3]:
            r3 += 1
               
    answer = []
    
    if r1 != 0:
        answer.append((r1, 1))
    if r2 != 0:
        answer.append((r2, 2))
    if r3 != 0:
        answer.append((r3, 3))
    
    answer.sort(reverse = True)
    
    result = []
    for ans in answer:
        if ans[0] == answer[0][0]:
            result.append(ans[1])
    result.sort()
    return result