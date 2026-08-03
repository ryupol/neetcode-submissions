class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_counter = Counter(s1)

        for i in range(len(s2) - len(s1) + 1):
            s2_counter = Counter(s2[i: i + len(s1)])
            if s1_counter == s2_counter:
                return True
        
        return False