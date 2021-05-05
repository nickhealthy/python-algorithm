import collections


n, m = map(int, input().split()) # 큐의 크기, 뽑아내려고 하는 수
element = collections.deque(list(map(int, input().split()))) # 뽑아내려고 하는 원소 값

count = 0 # 연산 횟수
queue = collections.deque(range(1, n + 1))

while True:
    if element and queue[0] == element[0]:
        queue.popleft()
        element.popleft()
        m -= 1
        continue
    
    try:
        value = queue.index(element[0])
    except:
        if count == 0:
            print(0)
        else:
            print(count)
        break

    # 앞으로 옮기는게 유리할 경우
    if value > len(queue) // 2:
        queue.rotate(len(queue) - value) # 앞에 있는 원소들을 'len(queue) - value' 값만큼 뒤로 보냄
        count += (len(queue) - value)
    # 뒤로 옮기는게 유리할 경우
    elif value <= len(queue) // 2:  
        queue.rotate(-value) # 뒤에 있는 원소들을 'value' 값만큼 앞으로 보냄
        count += value

    queue.popleft()
    element.popleft()
    m -= 1

    # 원하는 원소 값을 모두 찾은 경우
    if m == 0:
        print(count)
        break
