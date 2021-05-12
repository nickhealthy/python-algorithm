class Solution:
    def longestPalindrome(self, s):
        # 길이가 하나이거나, s 문자열 자체가 팰린드룸이라면
        if len(s) < 2 or s == s[::-1]:
            return s
        
        # 가장 긴 팰린드롬 체크
        def expand(left, right):
            while left >= 0 and right <= len(s) and s[left] == s[right - 1]:
                left -= 1
                right += 1
            return s[left + 1 : right - 1]

        result = ''
        for i in range(len(s) - 1):
             # 가장 긴 팰린드롬 선별
            result = max(result,
                        expand(i, i + 1), # 홀수 판별
                        expand(i, i + 2), # 짝수 판별
                        key=len) # 길이를 기준으로 max 값을 result에 대입

        return result
