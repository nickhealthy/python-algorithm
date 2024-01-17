import sys

input = sys.stdin.readline
orginal_strings = input().strip()
bomb_string = input().strip()

BOMB_STRING_LENGTH = len(bomb_string)

stack = []
for char in orginal_strings:
    stack.append(char)

    isBombStringCount = 0
    for j in range(BOMB_STRING_LENGTH):
        isBombStringCount += 1
        if stack[len(stack) - 1 - j] != bomb_string[BOMB_STRING_LENGTH - 1 - j]:
            break

    else:
        # 스택에 폭발 문자열이 들어있다면
        for _ in range(BOMB_STRING_LENGTH):
            stack.pop()

if stack:
    print("".join(stack))
else:
    print("FRULA")
