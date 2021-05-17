# 너비 우선 탐색

from collections import deque

n, k = map(int, input().split())
visited = [0 for _ in range(100001)] # 방문 표시용
queue = deque([[n, 0]]) # 현재 위치, 방문할 위치 초기화

while queue:
    pos, cnt = queue[0][0], queue[0][1]
    if pos == k:
        print(cnt)
        break

    visited[pos] = 1 # 현재 위치 방문 표시
    queue.popleft() # 다음 위치를 가기 위해 방문한 곳은 처리
    
    # pos 0 이상이고, 방문하지 않은 곳이라면
    if pos - 1 >= 0 and visited[pos - 1] == 0: 
        queue.append([pos - 1, cnt + 1]) # pos 값 누적, 몇번 방문했는지 카운트
    if pos + 1 <= 100000 and visited[pos + 1] == 0:
        queue.append([pos + 1, cnt + 1])
    if pos * 2 <= 100000 and visited[pos * 2] == 0:
        queue.append([pos * 2, cnt + 1])

