class Solution(object):
  def reverseString(self, s):
    """
    :type s: List[str]
    :rtype: void Do not return anything, modify s in-place instead.
    """
    t = len(s)
    for i in range(t/2):
      s[i],s[t-(i+1)] = s[t-(i+1)],s[i]

    # Comment return when posting to leetcode
    return s