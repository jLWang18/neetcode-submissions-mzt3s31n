class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        for left in range(len(heights)):
            for right in range(len(heights) - 1, left, -1):
                area = min(heights[left], heights[right]) * (right - left)
                res = max(res, area)
        return res