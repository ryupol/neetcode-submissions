class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res
        
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            num_str = ""
            while s[i] != '#':
                num_str += s[i]
                i += 1
            i += 1 # Skip '#'
            length = int(num_str)
            res.append(s[i:i + length])
            i += length
        return res
            


