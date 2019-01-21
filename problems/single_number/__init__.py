class Solution(object):
  def singleNumber(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    hash_table = {}
    for n in nums:
      if not hash_table.has_key(n):
        hash_table[n] = 0
      else:
        hash_table[n] = 1

    for n,t in hash_table.iteritems():
      if t == 0:
        return n
