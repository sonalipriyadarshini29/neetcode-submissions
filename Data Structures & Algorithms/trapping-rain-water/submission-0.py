class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0
        
        maxLeft = [0]*n
        maxRight = [0]*n
        summ = 0
        
        maxLeft[0] = height[0]
        for i in range(1,n):
            maxLeft[i] = max(height[i], maxLeft[i-1])
        
        maxRight[n-1] = height[n-1]
        for i in range(n-2,-1,-1):
            maxRight[i] = max(height[i], maxRight[i+1])
        
        for i in range(n):
            summ += min(maxLeft[i], maxRight[i]) - height[i]
        return summ
