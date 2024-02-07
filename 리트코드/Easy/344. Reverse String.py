"""
Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

"""

from typing import List


# 첫 번째 풀이
def reverseString1(s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    left, right = 0, len(s) - 1

    while left < right:
        s[left], s[right] = s[right], s[left],
        left += 1
        right -= 1


# 두 번째 풀이
def reverseString2(s: List[str]) -> None:
    # s.reverse()
    s = s[::-1]
