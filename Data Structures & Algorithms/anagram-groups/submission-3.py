class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # ["act","pots","tops"]
        # hashmap = {[0]x26: 0, [0]x26: 1}
        # res = [["act"], [pots, tops]]

        hashmap = {}
        res = []
        i = 0
        for word in strs:
            alp_count = [0] * 26
            for w in word:
                alp_index = ord(w) - ord("a")
                alp_count[alp_index] += 1

            alp_count_str = str(alp_count)
            
            if alp_count_str in hashmap:
                res[hashmap[alp_count_str]].append(word)
            else:
                res.append([word])
                hashmap[alp_count_str] = i
                i += 1
        return res

