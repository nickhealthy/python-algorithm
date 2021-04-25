import collections
import sys

input = sys.stdin.readline
test_cases = int(input().rstrip())

arr = collections.deque()
for _ in range(test_cases):
    process = input().rstrip().split()
    if process[0] == "push_front":
        arr.appendleft(process[1])
    if process[0] == "push_back":
        arr.append(process[1])
    if process[0] == "pop_front":
        try:
            print(arr.popleft())
        except:
            print(-1)
    if process[0] == "pop_back":
        try:
            print(arr.pop())
        except:
            print(-1)
    if process[0] == "size":
        print(len(arr))
    if process[0] == "empty":
        if len(arr) == 0:
            print(1)
        else:
            print(0)
    if process[0] == "front":
        try:
            print(arr[0])
        except:
            print(-1)
    if process[0] == "back":
        try:
            print(arr[-1])
        except:
            print(-1)