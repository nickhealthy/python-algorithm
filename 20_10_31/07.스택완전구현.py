## 함수 선언부
def isStackFull():
    global stack, top, SIZE
    if (top >= SIZE - 1):
        return True
    else:
        return False


def isStackEmpty():
    global stack, top, SIZE
    if (top <= -1):
        return True
    else:
        return False


def push(data):
    global stack, top, SIZE
    if (isStackFull()):
        print('스택 꽉참!!')
        return
    top += 1
    stack[top] = data


def pop():
    global stack, top, SIZE
    if (isStackEmpty()):
        print('스택 비었음')
        return
    data = stack[top]
    stack[top] = None
    top -= 1
    return data


## 전연 변수부
SIZE = 5
stack = [None for _ in range(SIZE)]
top = -1

## 메인 코드부
if __name__ == '__main__':
    pass

push('a')
push('b')
push('c')
push('d')
push('e')
push('f')
print(stack)
print(pop())
print(pop())
print(pop())
print(pop())
print(pop())
print(pop())
