import sys
import collections

read = sys.stdin.readline
n, m, v = map(int, read().split())
graph = [[0] * (n + 1) for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    line = list(map(int, read().split()))
    graph[line[0]][line[1]] = graph[line[1]][line[0]] = 1

def dfs(v):
    visited[v] = True # 방문 처리
    print(v, end=' ')
    for i in range(1, n + 1):
        if not visited[i] and graph[v][i] == 1:
            dfs(i)


def bfs(v):
    queue = collections.deque([v])
    visited[v] = False
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in range(1, n + 1):
            if visited[i] and graph[v][i] == 1:
                queue.append(i)
                visited[i] = False

dfs(v)
print()
bfs(v)
