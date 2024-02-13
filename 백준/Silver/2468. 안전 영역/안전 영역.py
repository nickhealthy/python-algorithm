import sys
from collections import deque
from typing import List, Deque

input = sys.stdin.readline


def bfs(i: int, j: int, h: int) -> None:
    q: Deque = deque()
    q.append((i, j))
    visited[i][j] = 1

    while q:
        ci, cj = q.popleft()

        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni = di + ci
            nj = dj + cj

            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0 and graph[ni][nj] > h:
                visited[ni][nj] = 1
                q.append((ni, nj))


N: int = int(input())
graph: List[List[int]] = [list(map(int, input().split())) for _ in range(N)]

answer: int = 0
for height in range(100):
    visited: List[List[int]] = [[0] * N for _ in range(N)]

    cnt = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0 and graph[i][j] > height:
                bfs(i, j, height)
                cnt += 1
                answer = max(answer, cnt)

print(answer)
