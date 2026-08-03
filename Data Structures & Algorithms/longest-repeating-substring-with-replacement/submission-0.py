class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        
        for l in range(len(s)):
            counter, max_f = defaultdict(int), 0
            for r in range(l, len(s)):
                counter[s[r]] += 1
                max_f = max(max_f, counter[s[r]])
                
                if max_f + k >= (r - l + 1):
                    res = max(res, r - l + 1)
        return res
                
                
            