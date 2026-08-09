class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setNum = set(nums)
        arr = []
        for i in setNum:
            if i-1 not in setNum:
                arr.append(i)
        maxLength = 0
        for i in arr:
            length = 1
            startingNum = i
            while startingNum+1 in setNum:
                length += 1
                startingNum += 1
            maxLength = max(maxLength, length)
        return maxLength
            
            


