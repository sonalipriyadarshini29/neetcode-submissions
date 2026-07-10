class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashset = defaultdict(list)
        for string in strs:
            count = [0]*26
            for char in string:
                count[ord(char)-ord("a")] += 1 #otherwise you would've sorted and that would take extra time
            hashset[tuple(count)].append(string)
        return list(hashset.values())

        