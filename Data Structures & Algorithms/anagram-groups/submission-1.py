class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # {act: [act, cat], aht: [hat], post: [stop, pots, tops]}

        # time complexity: O(n * m)

        hmap = defaultdict(list)
        for s in strs:
            counter = [0] * 26
            for c in s:
                counter[ord(c) - ord("a")] += 1
            hmap[tuple(counter)].append(s)
        
        res = []
        for ans in hmap.values():
            res.append(ans)

        return res

