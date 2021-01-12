# 1번 문자열 거꾸로 뒤집기
# Reversing a string using slicing

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
