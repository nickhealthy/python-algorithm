from collections import deque

def solution(box):
    days = -1

    while q:
        days += 1

        for _ in range(len(q)):
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if 0 <= nx < n and 0 <= ny < m and box[nx][ny] == 0:
                    q.append((nx, ny))
                    box[nx][ny] = box[x][y] + 1
    
    for b in box:
        if 0 in b:
            return -1
    
    return days

m, n = map(int, input().split()) # col, row
box, q = [], deque()
# 상하좌우
dx = [-1, 1, 0, 0] # row
dy = [0, 0, -1, 1] # col

for i in range(n):
    row = list(map(int, input().split()))
    for j in range(m):
        if row[j] == 1:
            q.append((i, j))
    box.append(row)

print(solution(box))
