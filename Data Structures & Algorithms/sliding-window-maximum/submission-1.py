class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        count = {}
        result = []
        l = 0
        for r in range(len(nums)):
            count[nums[r]] = 1+count.get(nums[r],0)
            if r >= k-1:
                result.append(max(count.keys()))
                count[nums[l]] = count.get(nums[l],0)-1
                if count[nums[l]]<=0:
                    count.pop(nums[l])
                l += 1
        return result
            


            