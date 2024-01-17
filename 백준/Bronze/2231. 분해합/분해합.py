import sys

input = sys.stdin.readline


def solution(N):
    for num in range(1, N):
        answer = 0

        for i in str(num):
            answer += int(i)

        if answer + num == N:
            return num

    return 0


N = int(input().strip())
print(solution(N))
