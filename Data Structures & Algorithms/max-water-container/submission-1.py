class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        maxArea = 0
        i = 0
        j = len(heights) - 1

        for i in range(len(heights)):
            for j in range(i + 1, len(heights)):
                area = (j-i) * min(heights[i], heights[j])
                maxArea = max(maxArea, area)
        return maxArea
        