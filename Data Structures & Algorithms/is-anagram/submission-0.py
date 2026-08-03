class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hmap = defaultdict(int) # O(26)
        for c in s:
            hmap[c] += 1

        for c in t:
            hmap[c] -= 1

            if hmap[c] < 0:
                return False
        return True
            