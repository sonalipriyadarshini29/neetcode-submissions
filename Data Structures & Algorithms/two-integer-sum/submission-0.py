class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complementary = {}
        for i in range(len(nums)):
            complementary[target-nums[i]]=i
        for i in range(len(nums)):
            if nums[i] in complementary and i<complementary[nums[i]]:
                return [i,complementary[nums[i]]]