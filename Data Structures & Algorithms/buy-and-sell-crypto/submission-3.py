class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lo, hi = 0, 0
        maxP = 0

        for i in range(len(prices)):
            if prices[i]<prices[lo]:
                lo = i
            else:
                hi = i
                maxP = max(maxP, prices[hi]-prices[lo])
        return maxP