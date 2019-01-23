from problems.plus_one import Solution

class Case(object):
  def __init__(self, digits, result):
    self.digits = digits
    self.result = result

tests = [
  Case([1,2,3], [1,2,4]),
  Case([4,3,2,1], [4,3,2,2]),
  Case([1,9,9], [2,0,0]),
  Case([9,9,9], [1,0,0,0]),
]

def test_solution():
  s = Solution()
  for t in tests:
    result = s.plusOne(t.digits)
    assert  result == t.result