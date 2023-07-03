def solution(n):
    answer = 0
    return sum([x for x in range(n + 1) if x % 2 == 0])