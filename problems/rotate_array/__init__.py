class Solution(object):
  def rotate(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    t = len(nums)
    k = k%t
    nums[:] = nums[t-k:] + nums[:t-k]

    # Return only for pytest. Comment when post to leetcode
    return nums