from problems.reverse_string import Solution

class Case(object):
  def __init__(self, s, result):
    self.s = s
    self.result = result

tests = [
  Case(["h","e","l","l","o"], ["o","l","l","e","h"]),
  Case(["H","a","n","n","a","h"], ["h","a","n","n","a","H"])
]

def test_solution():
  s = Solution()
  for t in tests:
    result = s.reverseString(t.s)
    assert  result == t.result