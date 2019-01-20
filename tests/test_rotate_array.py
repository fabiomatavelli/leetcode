from problems.rotate_array import Solution

class Case(object):
  def __init__(self, nums, k, result):
    self.nums = nums
    self.k = k
    self.result = result

tests = [
  Case([1,2,3,4,5,6,7], 3, [5,6,7,1,2,3,4]),
  Case([-1,-100,3,99], 2, [3,99,-1,-100])
]

def test_solution():
  s = Solution()
  for t in tests:
    result = s.rotate(t.nums, t.k)
    assert  result == t.result