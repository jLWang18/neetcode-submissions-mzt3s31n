class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        maxLeft, maxRight = heights[left], heights[right]
        area = 0
        while left < right:
            temp = min(maxLeft, maxRight) * (right - left)
            area = max(area, temp) 
            if maxLeft < maxRight:
                left += 1
                maxLeft = heights[left]
            else:
                right -= 1
                maxRight = heights[right]
        return area
