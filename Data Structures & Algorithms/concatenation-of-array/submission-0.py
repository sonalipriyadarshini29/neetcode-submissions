class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [num for num in nums]
        for num in nums:
            ans.append(num)
        return ans