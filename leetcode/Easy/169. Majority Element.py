'''
문제: 
최다 출현한 숫자 찾아서 리턴해라
이 숫자는 n//2 보다 많이 나온 숫자여야함

풀이:
sort한 다음에 중복횟수 기록해서 비교할 변수 만들어서 비교해가면서 하면 될듯?
'''

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        temp = 1        
        result = 0
        n = len(nums)
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                temp += 1
            else:
                if temp > result and temp > (n // 2): # 기존의 최대 중복 횟수였던 result와 새로갱신된 temp를 비교
                    result = nums[i]   # temp가 더 크므로 temp로 갱신
                    temp = 1           # 다시 temp 초기화 

        #  else문에 숫자가 바뀔때마다 검사하기 때문에
        #  만약 맨 마지막 숫자가 제일 많이 나왔다면 검사가 불가능해서 한번 더 해줌
        if temp > result and temp > (n // 2):
            result = nums[-1]
        return result