class Solution(object):
  def intersect(self, nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    
    found = []
    for n in nums1:
      if n in nums2:
        found.append(n)
        nums2.remove(n)

    return found