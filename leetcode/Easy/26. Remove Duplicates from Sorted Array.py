'''
https://leetcode.com/problems/remove-duplicates-from-sorted-array/?envType=study-plan-v2&envId=top-interview-150
26. Remove Duplicates from Sorted Array

문제:
중복값을 제거하고 k = 남은 요소의 개수를 리턴해라
순서는 유지해야한다, nums는 오름차순 정렬되어있다

풀이 1.
   set쓰면 중복 없어지니까 이거 쓰고 다시list로 만든담에 길이를 k에 저장하면 될거같다
    -> 원래 이거 되는건데 리트코드에서는 본인을 재선언 하는 방식은 안되는거같다?
풀이 2. for문 돌리면서 앞 뒤 값 바뀔때마다 temp += 1 해서 nums 위치정보로 쓰면 될거같다   
   temp = 0 으로 시작할거니까 마지막에 k = temp + 1 하면 될듯
'''       
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
          
        # nums = set(nums)
        # nums = list(nums)
        # k = len(nums)
        # return k
        temp = 0
        for i in range(len(nums)-1):
            if nums[i] != nums[i+1]:
                temp += 1
                nums[temp] = nums[i+1]
        k = temp + 1
        return k