from collections import deque

def dfs(v):
    visited[v] = True
    print(v, end=' ')
    for i in range(1, n + 1):
        if not visited[i] and graph[v][i] == 1:
            dfs(i)

def bfs(v):
    queue = deque([v])
    visited[v] = False
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in range(1, n + 1):
            if visited[i] and graph[v][i] == 1:
                queue.append(i)
                visited[i] = False


n, m, v = map(int, input().split()) # 정점, 간선, 시작점
visited = [False for _ in range(n + 1)] # 방문 설정
graph = [[0] * (n + 1) for _ in range(n + 1)]
# 매트릭 설정
for _ in range(m):
    line = list(map(int, input().split()))
    graph[line[0]][line[1]] = graph[line[1]][line[0]] = 1

dfs(v)
print()
bfs(v)