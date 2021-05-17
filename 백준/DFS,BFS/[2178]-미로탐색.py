from collections import deque

n, m = map(int, input().split())
num_map = [list(input()) for _ in range(n)]
queue = deque([[0, 0]])

dx = [1, -1, 0, 0] # row
dy = [0, 0, -1, 1] # col
num_map[0][0] = 1

while queue:
    x, y = queue[0][0], queue[0][1] # 이전 row, col 값 가지고 있음
    queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and num_map[nx][ny] == "1":
            queue.append([nx, ny])
            num_map[nx][ny] = num_map[x][y] + 1

print(num_map[n - 1][m - 1])