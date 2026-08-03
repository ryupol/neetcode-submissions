class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ""

        for i in range(len(s)):
            curr, counter = 0, Counter(t)
            for j in range(i, len(s)):
                if s[j] in counter and counter[s[j]] > 0:
                    counter[s[j]] -= 1
                    curr += 1

                if curr == len(t):
                    res = s[i:j+1]
                    break
        
        return res

                
                