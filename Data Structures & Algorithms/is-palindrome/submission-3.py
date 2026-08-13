class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = "abcdefghijklmnopqrstuvwxyz0123456789"
        char_set = set(chars)

        l = 0
        r = len(s) - 1

        s = s.lower()
        while l < r:
            while l < len(s) - 1 and s[l] not in char_set:
                l += 1
            
            while r >= 0 and s[r] not in char_set:
                r -= 1

            if s[l] != s[r]:
                return False

            l += 1
            r -= 1

        return True