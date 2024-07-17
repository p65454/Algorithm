# https://leetcode.com/problems/build-an-array-with-stack-operations/

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        '''
        문제) 1,2,3,4,5 , ... n 까지 증가하는데 이걸 push, pop 이용해서
        target과 똑같이 만들어줘야함
        push, pop 동작했던 순서가 들어있는 배열을 return해라        
        중간에 target과 일치할 시 조기 종료해라
        
        예를들어 ex1 인 target = [1,3] 이고 n = 3 이면
        push -> 1
        push, push -> 1, 2
        push, push, pop -> 1
        push, push, pop, push -> 1, 3
        
        풀이)
        조건을 보니 범위가 크지 않다. 그냥 example대로 동작을 그대로 구현하면 될듯
        구현문제같다?
        
        output : push, pop 넣을 배열
        array : 1~n 까지 생성할 배열
        cnt : push와 pop의 차이를 계산해서 target의 길이와 비교하기 위한 변수         
        '''
        
        output = []
        array = []        
        cnt = 0  

        for i in range(n):
            array.append(i+1)    # array에 1,2,3 이렇게 하나씩 넣어준다
            output.append("Push") # 넣는 동작 햇으므로 push 넣는다
            cnt += 1 # push 동작이 있을 때 마다 cnt는 1씩 증가
            if array[i] not in target: # target에 해당 숫자가 없다면
                output.append("Pop") 
                cnt -= 1 # pop 할 때 마다 cnt 는 1씩 감소
            if cnt == len(target): # 이 조건에 해당할 시 target과 같은 배열이 만들어짐
                break # 종료
        
        return output