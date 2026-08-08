class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1]*(n+1)
        postfix = [1]*(n+1)
        res = [1]*n
        runningProduct = 1
        for i in range(len(nums)):
            runningProduct *= nums[i]
            prefix[i+1] = runningProduct
        runningProduct = 1
        for i in range(n-1,-1,-1):
            runningProduct *= nums[i]
            postfix[i] = runningProduct
        for i in range(n):
            res[i]=prefix[i]*postfix[i+1]
        return res