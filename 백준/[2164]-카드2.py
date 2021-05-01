from collections import deque

n = int(input())
_list = list(range(1, n + 1))

queue = deque(_list)

while len(queue) != 1:
    queue.popleft()
    queue.append(queue.popleft())

print(queue.pop())