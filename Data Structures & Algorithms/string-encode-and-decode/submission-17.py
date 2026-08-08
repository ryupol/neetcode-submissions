class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i, s in enumerate(strs):
            res += str(len(s)) + "@" + s 
        return res

    def decode(self, s: str) -> List[str]:
        res = []

        i = 0
        while i < len(s):
            num_str = ""
            while s[i] != "@":
                num_str += s[i]
                i += 1
            i += 1 # Skip "@"
            word_length = int(num_str)
            res.append(s[i:i+word_length])
            i += word_length
        return res