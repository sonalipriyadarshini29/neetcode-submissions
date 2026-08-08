class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
         hashmap = Counter(nums)
         count = dict(sorted(hashmap.items(), key=lambda x: x[1], reverse=True))
         res = list(count.keys())[:k]
         return res
        