# Leetcode Problem 9: Palindrome Number

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        integer, reverse_integer = x, 0
        while x > 0:
            reverse_integer = (reverse_integer * 10) + x % 10
            x //= 10
        return integer == reverse_integer

# Time Complexity: O(log10(n))
# Space Complexity: O(1)

# Example:
# Input: x = 121
# Output: True