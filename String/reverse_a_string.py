# 1번 문자열 거꾸로 뒤집기
# Reversing a string using slicing

import collections
my_string = "ABCDE"
reversed_string = my_string[::-1]

print(reversed_string)

# Output
# EDCBA


# 2번 Palindrome 인지 판단
my_string = "abcba"

if my_string == my_string[::-1]:
    print("palindrome")
else:
    print("not palindrome")

# Output
# palindrome


# 3번 팰린드룸
def isPalindrome(S: str) -> bool:
    strs: Deque = collections.deque()

    for char in S:
        # 문자와 숫자 판별
        if char.isalnum():
            strs.append(char.lower())
    # 팰린드롬 여부 판별
    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False

    return True


print(isPalindrome("race a Car"))
