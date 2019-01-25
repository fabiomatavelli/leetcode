from problems.first_unique_character_in_a_string import Solution

class Case(object):
  def __init__(self, s, result):
    self.s = s
    self.result = result

tests = [
  Case("leetcode",0),
  Case("loveleetcode",2),
  Case("z",0),
  Case("dddccdbba",8)
]

def test_solution():
  s = Solution()
  for t in tests:
    result = s.firstUniqChar(t.s)
    assert  result == t.result