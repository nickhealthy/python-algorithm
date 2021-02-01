##함수 선언부
# 퀴즈 : 4시에 함께.... (신과 함께...)
def isQueueFull():  # T / F
    global SIZE, queue, front, rear
    if ((rear + 1) % SIZE == front):
        return True
    else:
        return False


def enQueue(data):
    global SIZE, queue, front, rear
    if (isQueueFull()):
        print('큐가 꽉참')
        return
    rear = (rear + 1) % SIZE
    queue[rear] = data


def isQueueEmpty():
    global SIZE, queue, front, rear
    if (front == rear):
        return True
    else:
        return False


def deQueue():
    global SIZE, queue, front, rear
    if (isQueueEmpty()):
        print('큐가 비었음')
        return
    front = (front + 1) % SIZE
    data = queue[front]
    queue[front] = None
    return data


## 전역 변수부
SIZE = 5
queue = [None for _ in range(SIZE)]
front = rear = 0

## 메인 코드부
enQueue('a')
enQueue('b')
enQueue('c')
enQueue('d')
enQueue('e')
print(queue)