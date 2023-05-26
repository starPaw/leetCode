from solution import Solution
import pytest


@pytest.mark.parametrize("a, expected", [("abcabcbb", 3), ("bbbbb", 1), ("pwwkew", 3)])
def test_solution(a, expected):
    result = Solution().lengthOfLongestSubstring(a)
    assert result == expected
