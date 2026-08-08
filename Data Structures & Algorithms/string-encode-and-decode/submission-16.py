class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i, s in enumerate(strs):
            res += s + "@" + str(len(s))
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        word = ""
        i = 0
        while i < len(s):
            if s[i] == "@":
                str_num = str(len(word))
                if str_num == s[i+1:i+1+len(str_num)]:
                    res.append(word)
                    word = ""
                    i += len(str_num)
                else:
                    word += s[i]
            else:
                word += s[i]
            i += 1
        return res