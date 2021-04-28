k = int(input())
stack = [0]

for i in range(k):
    n = int(input())
    if n == 0:
        stack.pop()
        continue
    stack.append(n)

print(sum(stack))