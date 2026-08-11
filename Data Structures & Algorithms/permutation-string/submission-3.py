class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        
        refCounter = Counter(s1)
        l, r = 0, len(s1)-1
        while r<len(s2):
            substring = s2[l:r+1]
            slidingCounter = Counter(substring)
            if refCounter == slidingCounter:
                return True
            l, r = l+1, r+1
        return False

        