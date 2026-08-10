class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        maxVol = 0 
        while l<r: 
            curVol = min(heights[l],heights[r])*(r-l)
            maxVol = max(maxVol, curVol)
            if heights[l]<heights[r]: 
                l+=1
            elif heights[r]<heights[l]:
                r-=1
            else: 
                l+=1
            
                
        return maxVol
            
        