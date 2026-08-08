class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numsMap = Counter(nums)
        majorityElementValue = max(numsMap.values())
        for i in numsMap:
            if numsMap[i]==majorityElementValue:
                return i
