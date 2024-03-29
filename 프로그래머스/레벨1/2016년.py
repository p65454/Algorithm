#
def solution(a, b):
    '''
    https://school.programmers.co.kr/learn/courses/30/lessons/12901
    
    문제) 2016년 1월 1일 은 금요일이다. 2016년은 윤년이다(2월이 29일까지 존재)
    a, b 두 수를 입력받아서 2016년 a월 b일이 무슨 요일인지 return해라
    답 형태 : SUN,MON,TUE,WED,THU,FRI,SAT 
    
    풀이1) 월별로 몇일까지 있는지 다르니까 새 리스트에 366일 요일정보 싹 다 넣고
    a월b일이 총 몇일인지 세서 그 위치를 찾으면 될것같다.
    '''
    day = ['SAT','SUN','MON','TUE','WED','THU','FRI'] # 0~6 : 월~일
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] # 각 월별로 최대 몇일까지 있는지
    array = ['FRI']
    n = 365
    
    while n > 0: # 1월1일인 금요일은 미리 넣고 시작하기 때문에 365번 돌리기
        for d in day: 
            array.append(d)
            n -= 1
            
    cnt = sum(month[:a-1]) + b # 총 몇일인지 계산    
    answer = array[cnt-1] 
          
    return answer
