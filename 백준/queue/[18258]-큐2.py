import collections
import sys


input = sys.stdin.readline

n = int(input().rstrip())
answer = collections.deque()
for _ in range(n):
    process = list(input().rstrip().split())
    if process[0] == "push":
        answer.append(process[1])
    if process[0] == "pop":
        try:
            print(answer.popleft())
        except:
            print(-1)
    if process[0] == "size":
        print(len(answer))
    if process[0] == "empty":
        if len(answer) == 0:
            print(1)
        else:
            print(0)
    if process[0] == "front":
        if len(answer) == 0:
            print(-1)
        else:
            print(answer[0])
    if process[0] == "back":
        if len(answer) == 0:
            print(-1)
        else:
            print(answer[-1])

