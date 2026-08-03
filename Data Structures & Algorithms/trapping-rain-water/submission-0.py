class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        res = 0 # Total Water

        max_h, water = 0, 0
        for i in range(n):
            if height[i] >= max_h:
                max_h = height[i]
                res += water
                water = 0
            else:
                water += max_h - height[i]

        max_h, water = 0, 0
        for i in range(n - 1, -1 , -1):
            if height[i] > max_h:
                max_h = height[i]
                res += water
                water = 0
            else:
                water += max_h - height[i]
        
        return res

        
