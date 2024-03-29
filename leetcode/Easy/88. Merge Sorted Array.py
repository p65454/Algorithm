# 88. Merge Sorted Array 
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:


        """
        Do not return anything, modify nums1 in-place instead.
        """
        '''
        m은 nums1 에서 0을 제외한 합칠 수 있는 요소의 갯수
        n은 nums2 에서 0을 제외한 합칠 수 있는 요소의 갯수
        return 쓰지말고 두 리스트를 nums1에다가 0빼고 다 합쳐서 오름차순으로 만들어라? 라고 해석됨         
        '''    
        # 일단 nums1 에 nums2 넣는다
        nums1.extend(nums2)       
        nums1.sort()
        if len(nums1) > m + n: # 이 조건문에 들어간다는것은 0이 포함되어 있다는 뜻
            while len(nums1) > m + n: # 0 없어질 때 까지 계속 0 삭제
                nums1.remove(0)

        # 결과 그래프를 보니 속도가 좀 느린편인 것 같다? 나중에 수정 