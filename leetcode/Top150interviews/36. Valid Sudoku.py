# https://leetcode.com/problems/valid-sudoku/?envType=study-plan-v2&envId=top-interview-150

from collections import defaultdict


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        '''
        문제) 스도쿠랑 동일한 규칙이고, 주어진 보드판을 스도쿠 규칙에 맞게 채울 수 있으면 true, 
        안되는게 있으면 false

        풀이) 생각하다가 안 떠올라서 솔루션 봄
        
        솔루션풀이) row, col, box 마다 숫자를 저장해가면서 중복을 체크하는 방식. 
        나도 이러한 방식을 떠올리긴 했는데 구체적으로 구현을 어떻게 해야할지 감이 안왔다.
        답을보니 dafultdict(set)을 사용해서 쉽게 해결한 솔루션이 있었다	       
        '''

        rows = defaultdict(set) # defaultdict(set)을 사용하게 되면 하나의 키 값에 여러 value들을 set형태로 저장할 수 있다
        cols = defaultdict(set)
        boxes = defaultdict(set)
        
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                
                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in boxes[(r // 3, c // 3)]:
                    return False
                
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                boxes[(r // 3, c // 3)].add(board[r][c])
        
        return True    