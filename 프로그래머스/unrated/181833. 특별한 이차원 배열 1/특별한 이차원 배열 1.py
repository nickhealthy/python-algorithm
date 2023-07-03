def solution(n):
    answer = [[0 if i != j else 1 for i in range(n)] for j in range(n)]
    return answer