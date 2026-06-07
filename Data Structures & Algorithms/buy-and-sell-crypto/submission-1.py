class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j=i+1
        maxP = 0 
        #buy,sell = prices[0],prices[1]
        while j<len(prices):
            if prices[j]>prices[i]:
                profit = prices[j]-prices[i]
                maxP = max(profit,maxP)
            else:
                i=j
            j+=1
        return maxP


         