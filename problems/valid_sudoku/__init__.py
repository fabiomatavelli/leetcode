class Solution(object):
  def isValidSudoku(self, board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """
    result = {}
    g = 0
    s = -3
    is_valid = True

    for i_r, r in enumerate(board):
      if i_r%3 == 0:
        s += 3
      
      if not result.has_key("r{0}".format(i_r)):
          result["r{0}".format(i_r)] = []

      for i_c, c in enumerate(r):
        if i_c%3 == 0:
          g += 1
        
        if not result.has_key(g+s):
          result[g+s] = []
        
        if not result.has_key("c{0}".format(i_c)):
          result["c{0}".format(i_c)] = []

        if c != ".":
          if c in result[g+s] + result["r{0}".format(i_r)] + result["c{0}".format(i_c)]:
            is_valid = False
            break

          result[g+s].append(c)
          result["r{0}".format(i_r)].append(c)
          result["c{0}".format(i_c)].append(c)
      
      g = 0

    return is_valid