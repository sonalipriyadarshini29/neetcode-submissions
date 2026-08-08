class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numsMap = Counter(nums)
        maxVal = max(numsMap, key=numsMap.get)
        return maxVal