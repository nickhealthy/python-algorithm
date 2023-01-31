import sys

input = sys.stdin.readline

N = int(input())
num_string = input().rstrip()

answer = 0
for i in range(N):
    # 문자열로 받기
    answer += int(num_string[i])

print(answer)
