class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        문제 : 인덱스 = 몇 일자 인지, 값 = 그 주식 가격
        언제 사서 언제 팔아야 최대 이익인가?
        두 수의 차이의 최대값을 찾아라

        풀이1) for문 2번써서 모든 차이를 저장하면 될거같다는 생각이 들었다 근데 범위를 보니까 시간초과 날수도?

        풀이2) 가장 작은수를 계속 갱신해 가면서 차이값을 빈 리스트에 계속 넣는다. 
        그 담에 마지막에 max() 해주면 될거 같다.

        '''
        array = [] # 차이값으로 사용할 리스트
        temp = prices[0] # 가장 작은 숫자를 기억할 임시 저장값으로 사용
        for i in range(len(prices)):
            if prices[i] > temp: # 가장 작은 숫자보다 클 때
                array.append(prices[i] - temp) # 차이를 기록
            else: 
                temp = prices[i] # temp 보다 더 작은 숫자가 나왔으므로 다시 갱신 

        if array:
            return max(array)

        return 0