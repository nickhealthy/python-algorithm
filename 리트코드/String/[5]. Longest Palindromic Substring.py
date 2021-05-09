class Solution:
    def longestPalindrome(self, s):
        # 길이가 하나이거나, s 문자열 자체가 팰린드룸이라면
        if len(s) < 2 or s == s[::-1]:
            return s
        
        # 가장 긴 팰린드롬 체크
        def expand(left, right):
            while left >= 0 and right <= len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1 : right]

        result = ''
        for i in range(len(s) - 2):
            result = max(result,
                        expand(i, i + 1), # 홀/짝에 따른 모든 경우의 수 체크를 위해 expand 2번 사용
                        expand(i, i + 2),
                        key=len) # 길이를 기준으로 max 값을 result에 대입

        return result

