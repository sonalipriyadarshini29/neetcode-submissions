class Solution:
    def isPalindrome(self, s: str) -> bool:
        validChars = set(range(ord('0'),ord('9')+1))
        validNums = set(range(ord('a'),(ord('z')+1)))
        clean_s = ''
        for i in s.lower():
            if ord(i) in validChars or ord(i) in validNums:
                clean_s += i
                
        l, r = 0, len(clean_s)-1
        while l<r:
            if clean_s[l]!=clean_s[r]:
                return False
            l, r = l+1, r-1
        
        return True