class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        hashmap = {0:0, 1:0, 2:0}
        for i in nums:
            hashmap[i]+=1
        for i in range(len(nums)):
            if i<hashmap[0]:
                nums[i] = 0
            elif i>=hashmap[0] and i<hashmap[0]+hashmap[1]:
                nums[i] = 1
            elif i>=hashmap[1] and i<hashmap[0]+hashmap[1]+hashmap[2]:
                nums[i] = 2
        