from problems.longest_common_prefix import Solution

class Case(object):
  def __init__(self, strs, result):
    self.strs = strs
    self.result = result

tests = [
  Case(["flower","flow","flight"],"fl"),
  Case(["dog","racecar","car"],""),
  Case(["a"],"a"),
  Case(["",""],""),
  Case(["c","c"],"c"),
  Case(["a","a","b"],""),
  Case([],""),
  Case(["abab","aba",""],""),
  Case(["aa","a"],"a")
]

def test_solution():
  s = Solution()
  for t in tests:
    result = s.longestCommonPrefix(t.strs)
    assert  result == t.result