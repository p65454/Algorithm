from collections import deque

n = int(input())
graph = [[] for i in range(n+1)]
for i in range(1, n+1):
    graph[i] = list(map(int, input().split()))

time = [0] * (n+1)
for i in range(1, n+1):
    time[i] = graph[i][0]

q = deque()
for i in range(1, n+1):
    if len(graph[i]) > 2:  # 선수 강의가 있는 경우
        result = []  # 선수 강의들의 시간들을 저장할 리스트
        for j in range(1, len(graph[i])-1):  # 해당 강의 자체의 시간과 -1은 제외(선수강의의 번호만 들여다본다)
            number = graph[i][j]
            q.append(number)
        while q:
            now = q.popleft()
            result.append(time[now])

        time[i] += max(result)  # 원래 시간에다 '선수강의중 최대로 오래 걸리는 시간' 만큼 더해줌

        # 정답이랑 방식이 다른데.. 이렇게 했을 때 안되는 테스트케이스가 있을까..? 입력예시는 답 나오는데.. 잘 모르겠다

for i in range(1, n+1):
    print(time[i])


'''
5
10 -1
10 1 -1
4 1 -1
4 3 1 -1
3 3 -1
'''