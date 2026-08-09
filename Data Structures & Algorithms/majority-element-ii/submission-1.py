class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hashmap = {}
        for i in nums:
            # registering the nums in the hashmap 
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
            # pruning to keep only 2 nums in the hashmap
            if len(hashmap)<3:
                continue
            else:
                indexes = list(hashmap.keys())
                for i in indexes:
                    hashmap[i] -= 1 #booyer moore algorithm
                    if hashmap[i] == 0:
                        hashmap.pop(i)
        # checking if the count is more than n//3 for top 2 candidates
        result = []
        for i in list(hashmap.keys()):
            if nums.count(i)>len(nums)//3:
                result.append(i)
        return result


            