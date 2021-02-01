ans = '수박'

# 내 풀이
def solution(n):
    for i in range(n+1):
        if n % 2 == 1:
            return (ans * (n//2)) + ans[0]
        else:
            return ans * (n//2)


# 다른 사람 풀이
def water_melon(n):
    s = "수박" * n
    return s[:n]
