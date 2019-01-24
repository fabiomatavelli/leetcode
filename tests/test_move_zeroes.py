from problems.move_zeroes import Solution

class Case(object):
  def __init__(self, nums, result):
    self.nums = nums
    self.result = result

tests = [
  Case([0,1,0,3,12], [1,3,12,0,0]),
  Case([0,0,0,1,2,3],[1,2,3,0,0,0]),
  Case([0],[0])
]

def test_solution():
  s = Solution()
  for t in tests:
    result = s.moveZeroes(t.nums)
    assert  result == t.result