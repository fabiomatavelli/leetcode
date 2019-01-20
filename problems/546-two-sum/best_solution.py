class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_table = {}
        for i, n in enumerate(nums):
            if hash_table.has_key(target-n):
                return sorted([i, hash_table[target-n]])
            else:
                hash_table[n] = i

        return []