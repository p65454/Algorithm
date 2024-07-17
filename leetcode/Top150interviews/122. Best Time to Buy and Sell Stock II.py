# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        조건을 보면 prices의 길이가 3 * 10^4 이므로 완전탐색 돌렸을 때 n^2 나온다고 치면
        10^9 정도 되기 떄문에 최대 10초 걸린다. (1억이 1초로 알고 있음)
        -> 너무 오래걸림
        
        뭔가 직감적으로 DP가 떠오른다..
        
				당일날 사서 팔수 있으니까 최대값을 비교해가면서 누적해서 DP테이블 갱신하면 될듯
				예를들어 ex1 의 배열인 [7,1,5,3,6,4] 일 때 
				dp[0] = 7-7 = 0 
				dp[1] = dp[0] 과 dp[0] + 1-7 을 비교한다. (쉽게 할려고 그냥 무조건 뒤에서 앞에거 뺌)
				dp[2] = dp[1] 과 , dp[1] + 5-1 를 비교한다.(4가 될것) 최대인걸로 하면 됨				
				
				이렇게 생각한 이유) 
				예를들어 [1, 2, 5, 6] 이렇게  있다고 했을 때
				1에서 사서 2에서 팔고, 2에서 사서 5에 팔고, 5에 사서 6에 팔고 하는거랑,
				1에서 사서 6까지 존버했다가 파는거랑 결과는 같기 때문이다.
				그러므로 순차적으로 차이를 구해서 더하면 최대값을 구할 수 있다고 생각함.
				....
				
				이런 방식으로 점화식을 작성해보면
				dp[i] = max(dp[i-1], dp[i-1] + prices[i] - prices[i-1]) 
				
        '''
        dp = [0 for _ in range(len(prices))]

				# dp[0] = 0 이므로 1부터 시작
        for i in range(1, len(dp)):
            dp[i] = max(dp[i-1], dp[i-1] + prices[i] - prices[i-1])
            
        return dp[-1] # 계속 누적해서 더한 맨 마지막이 최대값