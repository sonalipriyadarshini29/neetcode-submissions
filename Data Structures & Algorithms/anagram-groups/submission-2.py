class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for string in strs:
            temp = [0]*26
            for i in string:
                temp[ord(i)-ord('a')]+=1
            temp = tuple(temp)
            if temp in res:
                res[temp].append(string)
            else:
                res[temp] = [string]
        return list(res.values())
        