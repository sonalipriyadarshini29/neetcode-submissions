class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        pointer = 0
        maxLen = 0
        hashset = set()
        for i in range(len(s)):
            if s[i] in hashset:
                while s[pointer]!=s[i]:
                    hashset.remove(s[pointer])
                    pointer += 1
                pointer += 1
            else:
                hashset.add(s[i])
            maxLen = max(maxLen, i-pointer+1)
        return maxLen