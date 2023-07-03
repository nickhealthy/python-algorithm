from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def solution(maps):
    q = deque([(0, 0)])
    n, m = len(maps), len(maps[0])

    maps_count = [[0] * m for _ in range(n)]

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if maps[nx][ny] == 1 and maps_count[nx][ny] == 0:
                    maps_count[nx][ny] = 1
                    maps[nx][ny] = maps[x][y] + 1
                    q.append((nx, ny))

    return -1 if maps_count[-1][-1] == 0 else maps[-1][-1]

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))