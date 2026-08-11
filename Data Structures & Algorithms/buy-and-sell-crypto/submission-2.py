class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lo, hi = 0, 0
        maxP = 0

        for i in range(len(prices)):
            if prices[i]>prices[lo]:
                hi = i
                maxP = max(maxP, prices[hi]-prices[lo])
            else:
                lo = i
        return maxP