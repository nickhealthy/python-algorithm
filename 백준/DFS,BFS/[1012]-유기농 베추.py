from collections import deque

TC = int(input())

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0] # row
dy = [0, 0, -1, 1] # col

def bfs(x, y):
    q = deque([(x, y)])
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and map_list[nx][ny] == 1:
                q.append((nx, ny))
                visited[nx][ny] = True

for _ in range(TC):
    m, n, k = map(int, input().split()) # 가로, 세로, 배추 개수
    map_list = [[0] * (m) for _ in range(n + 1)]
    visited = [[False] * (m) for _ in range(n + 1)]
    
    for _ in range(k):
        line = list(map(int, input().split())) # 배추 위치
        map_list[line[1]][line[0]] = 1

    cnt = 0
    for i in range(n):
        for j in range(m):
            if visited[i][j] == 0 and map_list[i][j] == 1:
                cnt += 1
                bfs(i, j)

    print(cnt)