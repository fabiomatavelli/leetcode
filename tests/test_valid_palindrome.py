from problems.valid_palindrome import Solution

class Case(object):
  def __init__(self, s, result):
    self.s = s
    self.result = result

tests = [
  Case("", True),
  Case("A man, a plan, a canal: Panama", True),
  Case("race a car", False),
  Case("0P", False)
]

def test_solution():
  s = Solution()
  for t in tests:
    result = s.isPalindrome(t.s)
    assert  result == t.result