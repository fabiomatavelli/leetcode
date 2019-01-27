class Solution(object):
  def isPalindrome(self, s):
    """
    :type s: str
    :rtype: bool
    """
    if s == "":
      return True

    phrase = [c for c in s.lower() if c.isalnum()]
    if phrase == list(reversed(phrase)):
      return True

    return False