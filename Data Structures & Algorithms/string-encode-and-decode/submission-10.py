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
            i += 1 # Skip #
            count = int(num_str)
            substr = ""
            while count > 0:
                substr += s[i]
                count -= 1
                i += 1
            res.append(substr)
        return res
            


