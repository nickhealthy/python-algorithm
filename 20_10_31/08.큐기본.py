# 큐의 초기화
queue = [None, None, None]
front = rear = -1

rear += 1
queue[rear] = 'A'

rear += 1
queue[rear] = 'B'

front += 1
data = queue[front]
queue[front] = None
print(data)

rear += 1
queue[rear] = 'C'

front += 1
data = queue[front]
queue[front] = None
print(data)

front += 1
data = queue[front]
queue[front] = None
print(data)