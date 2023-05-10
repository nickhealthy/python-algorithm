from collections import deque


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def solution(maps):
    n, m = len(maps), len(maps[0])
    visited = [[0] * m for _ in range(n)]

    q = deque()
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S':
                q.append((i, j, 0))
                break

    lavel = False
    while q:
        x, y, cnt = q.popleft()

        if lavel and maps[x][y] == 'E':
            return cnt
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == 0 and maps[nx][ny] != 'X':
                    if maps[nx][ny] == 'L':
                        lavel = True
                        visited = [[0] * m for _ in range(n)]
                        visited[nx][ny] = 1
                        q = deque([(nx, ny, cnt + 1)])
                        break
                    else:
                        visited[nx][ny] = 1
                        q.append((nx, ny, cnt + 1))
        
    return -1