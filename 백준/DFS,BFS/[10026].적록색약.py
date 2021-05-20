from collections import deque

n = int(input())
map_list = [list(input()) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cnt = 0
cnt2 = 0

def bfs(x, y):
    q = deque([(x, y)])
    visited[x][y] = True
    while q:
        for _ in range(len(q)):
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                    if map_list[x][y] == map_list[nx][ny]:
                        visited[nx][ny] = True
                        q.append((nx, ny))
    global cnt
    cnt += 1
            
def another_bfs(x, y):
    q = deque([(x, y)])
    visited[x][y] = False
    while q:
        for _ in range(len(q)):
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < n and 0 <= ny < n and visited[nx][ny]:
                    if map_list[x][y] == map_list[nx][ny] or \
                        map_list[nx][ny] == 'R' and map_list[x][y] == 'G' or \
                        map_list[nx][ny] == 'G' and map_list[x][y] == 'R':
                        visited[nx][ny] = False
                        q.append((nx, ny))
    global cnt2
    cnt2 += 1


for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j)

for i in range(n):
    for j in range(n):
        if visited[i][j]:
            another_bfs(i, j)

print(cnt, end=' ')
print(cnt2)