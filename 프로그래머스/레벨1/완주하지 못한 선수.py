def solution(participant, completion):
    
    """"
    https://school.programmers.co.kr/learn/courses/30/lessons/42576
    
    선수의 수가 최대 10만이라서 for문 2번쓰면 시간초과 예상됨
    먼저 정렬시키고 for문 1번 돌리면서 각 리스트 요소를 순차적으로 비교해서 남는값을 정답으로 처리하자    
    """"
    
    p = sorted(participant)# sort, sorted 는 내부적으로 Nlog(N)의 시간복잡도 였던걸로 기억한다.. 아닐수도?
    c = sorted(completion)    
    
    for i in range(len(c)):
        # 완주자 리스트 길이만큼 돌면서 다른 이름이 있으면 완주를 못한사람이다.
        if p[i] != c[i]:
            return p[i]        
            
    return p[-1]   # 완주자 리스트를 다 돌았는데 아직 return이 안됐다? = 맨 마지막 사람이 답