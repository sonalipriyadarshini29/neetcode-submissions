class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        delim = "#"
        for string in strs:
            length = str(len(string))
            encoded_string += length+"#"
            encoded_string += string
        return encoded_string


    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        print(s)
        i = 0
        while i<len(s):
            j = i
            while s[j]!='#':
                j+=1
            length = int(s[i:j])
            temp = s[j+1:j+1+length]
            decoded_strs.append(temp)
            i = j+1+length
        return decoded_strs
