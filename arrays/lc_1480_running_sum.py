# Problem: Running Sum
# LeetCode: 1480
# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def runningSum(self, nums):
        for i in range(1, len(nums)):
            nums[i] = nums[i] + nums[i - 1]
        return nums
