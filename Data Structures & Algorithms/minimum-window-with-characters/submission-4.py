class Solution:
    def minWindow(self, s: str, t: str) -> str:
        have, countS, countT = 0, defaultdict(int), Counter(t)
        res, resLen = [-1, -1], float("infinity")

        l = 0
        for r in range(len(s)):
            c = s[r]
            countS[c] += 1

            if c in countT and countS[c] == countT[c]:
                have += 1

            while have == len(countT):
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                a = s[l]
                countS[a] -= 1
                if a in countT and countS[a] < countT[a]:
                    have -= 1
                l += 1
        l, r = res
        return s[l: r + 1] if resLen != float("infinity") else ""

                
                