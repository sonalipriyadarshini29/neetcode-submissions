class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        #covert all negatives to 0 and convert all 0 to len(nums)+1
        for i in range(n):
            if nums[i]<1:
                nums[i] = n+1

        #multiply -1 to nums[i] to represent i exists in nums while i belongs to [1,len(nums)+1]
        for i in range(n):
            val = abs(nums[i])
            if 1<=val<=len(nums) and nums[val-1]>0:
                nums[val-1] *= -1

        #iterate over the numbers from i = 1 to len(nums)+1 and return the first non-negative nums[i] 
        for i in range(1, len(nums)+1):
            if nums[i-1]>0:
                return i

        #return len(nums)+2 in case all numbers are distinct in nums and sequential when sorted
        return n+1
