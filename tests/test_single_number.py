from problems.single_number import Solution

class Case(object):
  def __init__(self, nums, result):
    self.nums = nums
    self.result = result

tests = [
  Case([2,2,1], 1),
  Case([4,1,2,1,2], 4),
  Case([4,3,2,1,3,2,1,3,2,1,5,6,4,5], 6)
]

def test_solution():
  s = Solution()
  for t in tests:
    result = s.singleNumber(t.nums)
    assert  result == t.result