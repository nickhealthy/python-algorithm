import sys
from collections import deque

def solution(numbers, target):
    answer = 0
    q = deque()
    q.append([numbers[0], 0])
    q.append([-1 * numbers[0], 0])
    n = len(numbers)
    
    while q:
        tmp, idx = q.popleft()
        idx += 1
        if idx < n:
            q.append([tmp + numbers[idx], idx])
            q.append([tmp - numbers[idx], idx])
        else:
            if tmp == target:
                answer += 1

    return answer

print(solution([1, 1, 1, 1, 1], 3))