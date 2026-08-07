class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        for i in s:
            if i in s_dict:
                s_dict[i] += 1
            else:
                s_dict[i] = 1
        for i in t:
            if i in s_dict and s_dict[i]>1:
                s_dict[i] -= 1
            elif i in s_dict and s_dict[i]==1:
                s_dict.pop(i)
            elif i not in s_dict:
                return False
        if s_dict == {}:
            return True
        else: 
            return False
                        