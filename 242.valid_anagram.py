# Leetcode problem - 242: Valid Anagram

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freq = {}
        for letter in s:
            freq[letter] = freq.get(letter, 0) + 1
        for letter in t:
            if letter not in freq:
                return False
            freq[letter] -= 1
            if freq[letter] < 0:
                return False
        return True

# Time Complexity: O(n)
# Space Complexity: O(n)/O(1) auxiliary space

# Example:
# Input: s = "anagram", t = "nagaram"
# Output: true