from problems.remove_duplicates_from_sorted_array import Solution

class Case(object):
  def __init__(self, nums, result):
    self.nums = nums
    self.result = result

tests = [
  Case([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 3, 4, 4, 5, 6, 7, 8], 9),
  Case([0, 1, 2, 3, 4, 5], 6),
  Case([], 0)
]

def test_solution():
  s = Solution()
  for t in tests:
    assert  s.removeDuplicates(t.nums) == t.result