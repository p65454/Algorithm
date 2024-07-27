# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/?envType=study-plan-v2&envId=top-interview-150
# 백트래킹

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        my_dict = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        result = []
        
        def backtrack(i, s):
            if i == len(digits):
                result.append(s)
                return                
            for c in my_dict[digits[i]]:
                backtrack(i+1, s+c)           
        if digits:
            backtrack(0, "")
        return result
