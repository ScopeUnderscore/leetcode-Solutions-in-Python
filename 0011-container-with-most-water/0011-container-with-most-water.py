class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        current_max_height = 0

        while left < right:
            width = right - left
            heights = min(height[left], height[right])
            current_area = width * heights

            current_max_height = max(current_max_height, current_area)
            if height[left] < height[right]:
                left +=1
            else:
                right -=1
        return current_max_height
        