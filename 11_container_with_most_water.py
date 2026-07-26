# Leetcode problem: 11 Container With Most Water

from ast import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_water = 0
        while l < r:
            area = min(height[l],height[r]) * (r-l)
            if area > max_water:
                max_water = area
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_water

# Time Complexity: O(n)
# Space Complexity: O(1)

# Example:
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
