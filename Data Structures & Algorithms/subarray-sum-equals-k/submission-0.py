class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefixSum = 0
        prefixHashMap = {0:1}
        for num in nums:
            prefixSum += num
            target = prefixSum - k
            if target in prefixHashMap:
                count += prefixHashMap[target]
            if prefixSum in prefixHashMap:
                prefixHashMap[prefixSum] += 1
            else:
                prefixHashMap[prefixSum] = 1
        return count 