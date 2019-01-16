class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        x = 0
        while x < len(nums)-1:
            y = x+1
            while y < len(nums):
                if (nums[x]+nums[y]) == target:
                    return [x, y]
                y += 1
            x += 1
            
