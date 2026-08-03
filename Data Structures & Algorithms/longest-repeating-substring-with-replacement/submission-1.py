class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        counter, max_f = defaultdict(int), 0
        res = 0

        l = 0
        for r in range(len(s)):
            counter[s[r]] += 1
            max_f = max(max_f, counter[s[r]])

            while max_f + k < (r - l + 1):
                counter[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
                
                
            