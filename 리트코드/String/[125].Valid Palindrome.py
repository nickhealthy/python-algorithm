from collections import deque

class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs: deque = deque()
        for char in s:
            if char.isalnum(): # char가 문자, 숫자면 참 or 거짓
                strs.append(char.lower())
        
        # 팰린드룸 판별 여부
        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False
        
        return True
