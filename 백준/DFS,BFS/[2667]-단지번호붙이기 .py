from collections import deque, Counter
from functools import reduce

n = int(input())
visited = [[0] * n for _ in range(n)]
map_list = [list(map(int, input())) for _ in range(n)]

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0] # row
dy = [0, 0, -1, 1] # col

def bfs(x, y, cnt):
    q = deque([[x, y]])
    visited[x][y] = cnt
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0 and map_list[nx][ny] == 1:
                visited[nx][ny] = cnt
                q.append((nx, ny))
            
cnt = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0 and map_list[i][j] == 1:
            cnt += 1
            bfs(i, j, cnt)

print(cnt) # 총 단지 갯수
ans = reduce(lambda x, y : x + y, visited, list()) # 1차원 배열로 통합
ans = [x for x in ans if x > 0] # 단지 개수가 포함된 것만 뽑아내기
ans = sorted(Counter(ans).values()) # 단지 별로 뭉친 개수를 뽑아내기
print("\n".join(map(str, ans)))