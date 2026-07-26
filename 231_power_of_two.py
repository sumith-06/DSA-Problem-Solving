# Leetcode problem: 231 Power of Two

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if (n > 0) and (n & (n-1) == 0):
            return True
        return False

# Time Complexity: O(1)
# Space Complexity: O(1)

# Example:
# Input: n = 1024 
# Output: True