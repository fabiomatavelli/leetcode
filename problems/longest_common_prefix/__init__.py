class Solution(object):
  def longestCommonPrefix(self, strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    i = 0
    for s in zip(*strs):
      if len(set(s)) > 1:
        return strs[0][:i]
      i += 1
    
    return strs[0][:i] if strs else ""
