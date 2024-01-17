import sys
from collections import deque

input = sys.stdin.readline
string = list(input().rstrip())
bomb = list(input().rstrip())

stack = deque()
bomb_length = len(bomb)
string_length = len(string)


for i in range(string_length):
    stack.append(string[i])
    # 폭탄 문자열 확인
    while True:
        flag = False

        if string_length < bomb_length:  # bomb_length가 더 길다면
            break

        for i in range(bomb_length):
            if stack[len(stack) - 1 - i] != bomb[bomb_length - 1 - i]:
                flag = True
                break

        if flag:
            break

        # 위의 폭탄 문자열을 확인해봤을 때 여기까지 넘어오면 폭탄 문자열이 포함되어 있다는 뜻
        # 폭탄 문자열 수만큼 스택 팝
        for _ in range(bomb_length):
            stack.pop()

        break


if not stack:
    print('FRULA')
else:
    print("".join(stack))