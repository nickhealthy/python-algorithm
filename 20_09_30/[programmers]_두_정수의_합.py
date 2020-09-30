a = 3
b = 5

# 내 풀이
def solution(a, b):
    if a > b: a, b = b, a
    return sum(range(a, b+1))
