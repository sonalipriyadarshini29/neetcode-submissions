class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        
        refCounter = Counter(s1)
        slidingCounter = Counter(s2[0:len(s1)])
        if refCounter == slidingCounter:
            return True

        l, r = 0, len(s1)-1
        while r<len(s2)-1:
            slidingCounter[s2[l]]-=1
            if slidingCounter[s2[l]]==0:
                slidingCounter.pop(s2[l])
            l, r = l+1, r+1
            slidingCounter[s2[r]] = 1 + slidingCounter.get(s2[r],0)
            if refCounter == slidingCounter:
                return True
        return False

        