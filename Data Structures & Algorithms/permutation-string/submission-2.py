class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ref_count = Counter(s1)
        for l in range(len(s2)-len(s1)+1):
            sliding_count = Counter(s2[l:l+len(s1)])
            if sliding_count == ref_count:
                return True
        return False