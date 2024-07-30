'''
 
 참고링크) https://bomoto.tistory.com/164

    문제) 1~6칸 이동가능한데, 지그재그로 이동하면서 사다리or뱀을 만나면 그 도착지로 이동해야한다.
    1에서 n*n까지 도착하는데 필요한 최소횟수를 구해라.
    (불가능시 -1)

    내 풀이) bfs로 풀면 될거 같다는 생각을 했고, 방문했는지 기록을 해야하나?에 대한 의문이 있었음(근데 하는게 효율적이다 이건 잘못된 생각이었음. bfs 자체가 애초에 재방문하지 않음으로써 최적의 경로를 찾는것)
    주사위를 1번던져서 갈 수 있는 범위를 확인하기 위해 cnt를 사용했고
    result에 주사위 던진 횟수를 기록했다.
    -> 결론 : 뭔가 잘 안된다.. 모든 경우에 대해서 답이 나오지 않는 것 같음. 좌표로 이용해서 생각하려니까 복잡함
 
  솔루션) 
  예시상황처럼 예를들어 n = 6  일 때 1~36까지의 숫자를 각각 좌표로 변환해주는 함수를 따로 만들고, 
  큐에다가 문제의 조건에 따라 1~36까지 그 숫자로 넣어버린다. 이렇게 하면서 방문하지 않은 곳만 들르면서 가면 
  복잡하지 않고 쉽게 접근 가능.

  예를들어 32와같은 숫자를 좌표로 변환하는 작업은 뱀or사다리를 만났을 때만 필요한 작업임

  
  아직 이해 안되는 점 ) example2 의 답이 왜 2가 아니고 1인지 모르겠음
'''



class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
    
        def getCoordinate(pos):
            r, c = divmod(pos-1, n)  # 좌표별 라벨이 1베이스라서 인덱스 구하기 위해 pos에서 1뺌
                                                        # divmod(a, b) 는 a를 b로 나눈 몫, 나머지를 반환한다.
            c = (n-1)-c if r%2==1 else c  # 몫이 짝수인 경우와 홀수인 경우 col이 어디서 시작하는지 달라서 따로 처리
            r = (n-1)-r
            return r, c
                
        n = len(board)
        q = [1]
        visited = set()
        step = 0
        
        while q:
            temp = []
            for curr in q:
                row, col = getCoordinate(curr)
                if board[row][col] != -1:  # 있는곳이 뱀이나 사다리라면?
                    curr = board[row][col]  # 해당위치로 이동
                if curr == n*n: return step  # 끝에 다다르면 리턴
                for i in range(1, 7):
                    nexts = curr + i
                    if nexts <= n*n and nexts not in visited:
                        temp.append(nexts)
                        visited.add(nexts)
            step += 1
            q = temp[:] # 전체의 요소를 슬라이싱하여 새로운 리스트로 복사함( 둘은 다른 개체)
        
        return -1