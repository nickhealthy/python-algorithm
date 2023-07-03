from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def solution(rows, columns, max_virus, queries):
    answer = [[0] * columns for _ in range(rows)]

    q = deque(queries)
    while q:
        x, y = q.popleft()
        x -= 1
        y -= 1

        # 세균이 max_virus 미만인 경우
        if answer[x][y] < max_virus:
            answer[x][y] += 1

        # 세균이 max_virus인 경우
        elif answer[x][y] == max_virus:
            # 주변에 세균 증식이 가능한 정보를 담는 배열
            virus_proliferate_arr = deque([(x, y)])
            # 중복 방문을 피하기 위한 체크 배열
            visited = [[0] * columns for _ in range(rows)]
            while virus_proliferate_arr:
                vx, vy = virus_proliferate_arr.popleft()

                for i in range(4):
                    nx = dx[i] + vx
                    ny = dy[i] + vy

                    # 가능한 경로인지 체크
                    if 0 <= nx < rows and 0 <= ny < columns:
                        # 각 칸의 virus 수 확인 및 증식
                        if visited[nx][ny] == 0 and answer[nx][ny] < max_virus:
                            visited[nx][ny] = 1
                            answer[nx][ny] += 1

                        elif visited[nx][ny] == 0 and answer[nx][ny] == max_virus:
                            visited[nx][ny] = 1
                            virus_proliferate_arr.append((nx, ny))

    return answer


# 다른 코드
# def solution(rows, columns, max_virus, queries):

#     grid = [[0]*columns for _ in range(rows)]

#     def action(i, j):
#         stack = [(i, j)]
#         visited = set([(i, j)])
#         while stack:
#             i, j = stack.pop()
#             if grid[i][j] < max_virus:
#                 grid[i][j] += 1
#             else:
#                 for _i, _j in [(i, j+1), (i, j-1), (i+1, j), (i-1, j)]:
#                     if 0 <= _i < rows and 0 <= _j < columns and (_i, _j) not in visited:
#                         visited.add((_i, _j))
#                         stack.append((_i, _j))

#     for i, j in queries:
#         action(i-1, j-1)

#     return grid


print(solution(3, 4, 2, [[3, 2], [3, 2], [2, 2],
      [3, 2], [1, 4], [3, 2], [2, 3], [3, 1]]))
