# 1. 학생들 자리배치를 먼저 해준다.
# 1-1. 인접해 있는 좋아하는 친구들 배치 카운트, 인접한 자리 중 빈 자리 개수 새기
# 1-2. 좋아하는 친구들이 많은 수가 있으면 해당 자리로 배치, 좋아하는 친구가 동등하다면 인접한 자리가 많은 자리로 들어가기

from collections import defaultdict

dx = [-1, 1, 0, 0] # row
dy = [0, 0, -1, 1] # col

n = int(input())
arr = [[0] * n for _ in range(n)]

student_list = defaultdict(list)
for _ in range(n ** 2):
    _input = list(map(int, input().split()))
    student_list[_input[0]] = _input[1:]
    max_like = -1
    max_empty = -1

    # 순차적으로 모두 탐색하면서 '좋아하는 친구', '빈자리 따로 계산'
    # 내가 좋아하는 애들이나 자리가 빈 곳을 각각 탐색하면서 4방향 모두 탐색해야함
    for x in range(n):
        for y in range(n):
            if arr[x][y] == 0:
                like = 0
                empty = 0
                
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]

                    if 0 <= nx < n and 0 <= ny < n:
                        if arr[nx][ny] in _input:
                            like += 1
                        if arr[nx][ny] == 0:
                            empty += 1
                # 해당 포지션에서 4방향을 확인했을 때, 최종적으로 들어갈 자리를 max_x, max_y에 갱신
                # 좋아하는 친구가 많은 자리 확인, 좋아하는 친구 수가 같으면 빈자리 많은 곳 확인 및 갱신
                if max_like < like or (max_like == like and max_empty < empty):
                    max_x = x
                    max_y = y
                    max_like = like
                    max_empty = empty
    
    arr[max_x][max_y] = _input[0]

# 2. 학생들의 만족도 조사
# 2.1 (1, 1)학생부터 차례대로 인접한 자리를 조사해서, 자신이 좋아하는 학생들이 인접해있다면 계산
# 결과 반환

result = 0
for x in range(n):
    for y in range(n):
        cnt = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                # 범위를 초과하지 않았다면, 인접자리(nx, ny)에 자신이 좋아하는 학생이 있는지 확인
                if arr[nx][ny] in student_list[arr[x][y]]:
                    cnt += 1

        if cnt != 0:
            result += 10 ** (cnt - 1)

print(result)