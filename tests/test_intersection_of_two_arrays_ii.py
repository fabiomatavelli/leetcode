from problems.intersection_of_two_arrays_ii import Solution

class Case(object):
  def __init__(self, nums1, nums2, result):
    self.nums1 = nums1
    self.nums2 = nums2
    self.result = result

tests = [
  Case([1,2,2,1], [2,2], [2,2]),
  Case([4,9,5], [9,4,9,8,4], [4,9])
]

def test_solution():
  s = Solution()
  for t in tests:
    result = s.intersect(t.nums1, t.nums2)
    assert  result == t.result