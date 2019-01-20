class Solution(object):
  def containsDuplicate(self, nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    table = set(nums)
  
    return len(table) != len(nums)