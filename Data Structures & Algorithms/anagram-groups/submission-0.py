class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashset = {}
        for i in strs:
            key = "".join(sorted(i))
            if key not in hashset:
                hashset[key] = [i]
            else:
                hashset[key].append(i)
        return [hashset[i] for i in hashset]