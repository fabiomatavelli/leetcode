class Solution(object):
  def plusOne(self, digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    for i in reversed(range(len(digits))):
      digits[i] += 1
      if digits[i] >= 10:
        digits[i] = 0
        if i == 0:
          digits.insert(0, 1)
      else:
        break

    return digits