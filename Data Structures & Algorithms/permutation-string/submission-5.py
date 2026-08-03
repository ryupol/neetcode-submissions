class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        char1, char2 = [0] * 26, [0] * 26

        for i in range(len(s1)):
            char1[ord(s1[i]) - ord("a")] += 1
            char2[ord(s2[i]) - ord("a")] += 1

        matched = 0
        for i in range(26):
            if char1[i] == char2[i]:
                matched += 1
        
        l = 0
        for r in range(len(s1), len(s2)):
            if matched == 26:
                return True

            index = ord(s2[r]) - ord("a")
            char2[index] += 1
            if char2[index] == char1[index]:
                matched += 1
            elif char2[index] == char1[index] + 1:
                matched -= 1

            index = ord(s2[l]) - ord("a")
            char2[index] -= 1
            if char2[index] == char1[index]:
                matched += 1
            elif char2[index] == char1[index] - 1:
                matched -= 1
            l += 1

        return matched == 26 