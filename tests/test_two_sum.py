from problems.two_sum import Solution

class Case(object):
  def __init__(self, nums, target, result):
    self.nums = nums
    self.target = target
    self.result = result

tests = [
  Case([2,7,11,15], 9, [0, 1]),
  Case([5,2,3,10,4,8], 12, [1, 3]),
  Case([2,3,6,7,4,1], 5, [0, 1]),
  Case([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20], 39, [19, 20]),
  Case([3,2,4], 6, [1, 2])
]

def test_solution():
  s = Solution()
  for t in tests:
    result = s.twoSum(t.nums, t.target)
    assert  result == t.result