class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        '''
        문제:
        리스트 nums에서 정수 val에 해당하는 숫자를 지워라
        nums에 남은 요소의 갯수를 k에 넣어서 리턴해라

        nums 리스트 for문 한바퀴 돌면서 temp = 위치정보 로 만들어서
        val 아닐 때만 temp +=1 해서 위치 한칸씩 늘려주면 된다 
        k개 이후의 요소는 뭐가오든 상관없다고 해서 가능한 느낌
        '''
        temp = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[temp] = nums[i] 
                temp += 1              
        k = temp
        return k