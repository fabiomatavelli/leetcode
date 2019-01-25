class Solution(object):
  def firstUniqChar(self, s):
    """
    :type s: str
    :rtype: int
    """
    d = set()
    for c in list(s):
      if c in d:
        continue
      
      p1 = s.find(c)
      p2 = s.rfind(c)
      if p1 == p2:
        return p1
      else:
        d.add(c)

    return -1