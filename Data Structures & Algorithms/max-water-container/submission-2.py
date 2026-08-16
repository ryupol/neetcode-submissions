class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # height = [1,7,2,5,4,7,3,6]

        # [5,8,1,1,9,5]

        res = 0
        l, r = 0, len(heights) - 1
        while l < r:
            h_left, h_right = heights[l], heights[r]
            res = max(res, (r - l) * min(h_left, h_right))

            if h_left < h_right:
                l += 1
            else:
                r -= 1
        
        return res
