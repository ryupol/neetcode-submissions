class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        for i in range(len(s2) - len(s1) + 1):
            substr = s2[i:i + len(s1)]

            if sorted(substr) == sorted(s1):
                return True
        
        return False