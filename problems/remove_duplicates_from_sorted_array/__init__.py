class Solution(object):
  def removeDuplicates(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    hash_table = {}
    i = 0
    while i < len(nums):
      if not hash_table.has_key(nums[i]):
        hash_table[nums[i]] = True
        i += 1
      else:
        nums.pop(i)

    return len(nums)