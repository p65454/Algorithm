from collections import deque

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        문제 : 오른쪽으로 한칸씩 땡길건데 k번 만큼 수행해라

        풀이1)
        큐를써서 뒤에꺼 빼고 앞에 넣으면 될거같다
        큐 어떻게 쓰더라? 해서 명령어 찾아보다 보니 deque.rotate로 한번에 풀릴거같다.
        deque으로 바꾸면 동작들이 시간복잡도가 엄청 낮았던 걸로 기억한다
        """

        q = deque(nums)  
        n = len(nums)
        k %= n   # 만약 k가 nums의 길이보다 훨씬 클 경우 쓸데없는 동작을 방지 -> 해보니까 k는 값 바꿔서 써도 되나보다
        q.rotate(k)
        list_q = list(q)

        for i in range(n):  # 원래 nums = list(nums) 로 하고 싶었는데 안되길래 이런식으로 넣어줌
            nums[i] = list_q[i]   