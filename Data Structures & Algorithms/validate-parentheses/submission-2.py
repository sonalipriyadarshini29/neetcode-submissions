class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {'{':'}','(':')','[':']'}
        if len(s)%2!=0:
            return False
        for i in s:
            if i in hashmap.keys():
                stack.append(i)
            else:
                if stack and hashmap[stack[-1]] == i:
                    stack.pop()
                else:
                    return False
        return True and stack==[]
