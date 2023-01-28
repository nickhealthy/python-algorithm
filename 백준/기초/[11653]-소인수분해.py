import sys

input = sys.stdin.readline

N = int(input())
answer = []

i = 2
while N != 1:
    while N % i == 0:
        answer.append(i)
        N //= i
    i += 1

answer.sort()
for i in answer:
    print(i)
