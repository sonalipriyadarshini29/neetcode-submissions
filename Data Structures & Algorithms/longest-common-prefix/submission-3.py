class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        currStr = strs[0]
        for string in strs[1:]:
            if currStr != string:
                maxLength = min(len(string), len(currStr))
                if maxLength == 0:
                    return ""
                for i in range(maxLength):
                    if currStr[i] == string[i]:
                        continue
                    elif currStr[i] != string[i]:
                        currStr = currStr[:i]
                        break  
                if len(currStr) > maxLength:
                    currStr = currStr[:maxLength]
        return currStr
            