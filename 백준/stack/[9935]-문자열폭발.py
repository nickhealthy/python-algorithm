import sys


input = sys.stdin.readline

word = list(input().strip())
bomb = list(input().strip())

word_length = len(word)
bomb_length = len(bomb)

stack = []
for i in range(word_length):
    stack.append(word[i])

    while True:
        flag = False

        for j in range(bomb_length):
            if stack[len(stack) - 1 - j] != bomb[len(bomb) - 1 -j]:
                flag = True
                break

        if flag:
            break

        for _ in range(bomb_length):
            stack.pop()

        break

if not stack:
    print('FRULA')
else:
    print("".join(stack))