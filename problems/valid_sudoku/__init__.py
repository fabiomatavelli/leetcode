class Solution(object):
  def isValidSudoku(self, board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """
    result = set()
    g = 0
    s = -3
    is_valid = True

    for i_r, r in enumerate(board):
      if i_r%3 == 0:
        s += 3

      if not is_valid:
        break

      for i_c, c in enumerate(r):
        if i_c%3 == 0:
          g += 1

        if c != ".":
          if (g+s,c) in result or ("r{0}".format(i_r),c) in result or ("c{0}".format(i_c),c) in result:
            is_valid = False
            break

          result.add((g+s,c))
          result.add(("r{0}".format(i_r),c))
          result.add(("c{0}".format(i_c),c))
      
      g = 0

    return is_valid