class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t):
            return ""

        target = Counter(t)
        string = ""
        result = ""
        resultLength = float('inf')
        l = 0
        freq = {}
        for r in range(len(s)):
            string += s[r]
            if s[r] in target:
                freq[s[r]] = freq.get(s[r], 0) + 1
            if len(freq)==len(target) and all([target[k]<=freq[k] for k in target]):
                while s[l] not in target or target[s[l]]<freq[s[l]]:
                    if s[l] in freq:
                        freq[s[l]] -= 1
                    l += 1
                if r - l + 1 < resultLength:
                    result = s[l:r+1]
                    resultLength = r - l + 1
        return result


        



