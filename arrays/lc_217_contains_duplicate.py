# Problem: Contains Duplicate
# LeetCode: 217
# Approach: Use a set to track seen elements
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def containsDuplicate(self, nums):
        seen = set()
        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        return False
