class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyPrice=prices[0]
        maxi=0
        for i in range(len(prices)):
            if buyPrice>prices[i]:
                buyPrice=prices[i]
            maxi=max(maxi,prices[i]-buyPrice)
        return maxi