'''
문제 : 
중복을 최대 1번까지만 나타나게 하고 그 중복된 숫자 종류가 몇개인지 k에 저장해서 리턴해라
nums 기본으로 오름차순 되어있고, k 개 이후의 배열상태는 상관 x


풀이 1. temp1에 위치정보 저장해서 중복1번 or 앞뒤 숫자 바뀔때마다 +1 해주고
        이 행동을 할지말지 판단할 변수 temp2 를 만들어서
        temp2가 0이면 하고 1이면 안하게 만들면 될거같다
        그리고 마지막에 k = temp1 + 1 하면 될듯
'''
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        temp1 = 0
        temp2 = 0
        for i in range(len(nums) - 1):            
            if nums[i] == nums[i+1] and temp2 == 0:
                temp1 += 1
                temp2 += 1                
                nums[temp1] = nums[i+1]
                
            elif nums[i] != nums[i+1]:
                temp1 += 1
                nums[temp1] = nums[i+1]
                temp2 = 0
        k = temp1 + 1
        return k