# https://leetcode.com/problems/valid-palindrome/solutions/3864359/python-3-two-solutions-beats-99-33ms/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        문제) 문장을 거꾸로 읽어도 원래 문장이랑 같은지 검사해서 같으면 true, 아니면 false 반환해라

        풀이)    
        1. 특수문자 없애고 소문자로 바꾸기
        2. s를 list로 바꿔서 각 요소마다 하나씩 들어가게하기
        3. list의 길이의 절반 ( len(array) // 2 ) 만큼을 계산해서 그때까지 for문 돌리면서
         앞뒤를 비교하기 if array[i] == array[-i-1] 
        
        ex) 'abcba' 이면 ab까지만 검사 (홀수개 일 때 가운데는 뭐든 상관없으므로)
            'abccba' 이면 abc까지만 검사
        
        그런데 이거 two pointer 문제인데.. 
        처음해보는 유형인데 이 방식이 맞는진 모르겠다
        '''

        s_clean = re.sub(r'[^a-zA-Z0-9]', '', s)
        array = list(s_clean.lower())        
        half_len = len(array) // 2
        
        for i in range(half_len):
            if array[i] != array[-i-1]:
                return False
        
        return True