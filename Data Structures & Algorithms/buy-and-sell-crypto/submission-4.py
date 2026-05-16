class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_n = prices[0]
        max_n = 0
        answer = 0 if len(prices) == 1 else -1
        flag= 0
        for i in range(1,len(prices)):
            if min_n > prices[i]:
                min_n = prices[i]
                max_n = 0 
            
            if max_n < prices[i]:
                max_n = prices[i]
                flag = 1

            if answer < max_n-min_n and flag== 1:
                answer = max_n-min_n
                flag = 0
            print('min_n : ', min_n)
            print('max_n : ', max_n)

            
        return answer