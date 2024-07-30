# https://leetcode.com/problems/search-a-2d-matrix/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        탐색인데 시간복잡도가 O(log(m * n)) 이내여야 한다. (완전탐색 으로는 불가능) 
        -> row, column 각각 이진탐색으로 돌리면 O(log(m)) + O(log(n)) = O(log(m * n)) 으로 계산가능

        row먼저 구하고 column 구하는 식으로 2번 돌려보자

        '''

        if target > matrix[-1][-1] or target < matrix[0][0]:
            return False
        
        left = 0
        right = len(matrix) - 1
        index = -1

        while left <= right:
            mid = left + (right - left) // 2
            if matrix[mid][0] <= target <= matrix[mid[-1]]:
                left = 0
                right = len(matrix[mid]) - 1
                index = mid
                break
            elif matrix[mid][0] < target:
                left = mid + 1
            else:
                right = mid - 1


        while left <= right:
            mid = left + (right - left) // 2
            if matrix[index][mid] == target:
                return True
            elif matrix[index][mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False