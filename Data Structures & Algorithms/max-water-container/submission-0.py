class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0, len(heights) -1
        global_sum = 0
        local_sum = 0
        while l < r:
            local_sum = min(heights[l],heights[r]) * (r-l)
            global_sum = max(global_sum, local_sum)
            
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
            
        return global_sum