# Problem: Two Sum
# LeetCode: 1
# Approach:
# Use a hash map to store number -> index.
# For each element, compute complement = target - num.
# If complement exists in map, return indices.
# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def twoSum(self, nums, target):
        seen = {}   
        
        for i, num in enumerate(nums):
            complement = target - num
            
            if complement in seen:
                return [seen[complement], i]
            
            seen[num] = i
