class Solution(object):
  def moveZeroes(self, nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    t = len(nums)
    n = 0
    zidx = -1
    for n in range(t):
      if nums[n] != 0:
        if zidx > -1:
          nums[zidx], nums[n] = nums[n], nums[zidx]
          zidx += 1
      else:
        if zidx == -1:
          zidx = n

    # Comment the return when posting to leetcode
    return nums