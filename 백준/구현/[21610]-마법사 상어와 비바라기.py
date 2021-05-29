n, m = map(int, input().split())
dx = [0, 0, -1, -1, -1, 0, 1, 1, 1] # row 1 ~ 8
dy = [0, -1, -1, 0, 1, 1, 1, 0, -1] # col 1 ~ 8

arr = [list(map(int, input().split())) for _ in range(n)]
# 구름 생성
clouds = [(n - 2, 0), (n - 2, 1), (n - 1, 0), (n - 1, 1)]

for i in range(1, m + 1):
    pos = []
    # 이동 입력
    _input = list(map(int, input().split()))
    # step 1
    for cloud in clouds:
        row = 0
        col = 0
        for j in range(_input[1]): # 움직임 횟수
            row += dx[_input[0]]
            col += dy[_input[0]]

        nx = (n + cloud[0] + row) % n
        ny = (n + cloud[1] + col) % n

        # step 2, 3
        visited = [[False] * n for _ in range(n)]
        arr[nx][ny] += 1
        visited[nx][ny] = True
        pos.append([nx, ny]) # 대각선 계산을 위한 배열
        # clouds = []
    
    # step 4
    for idx in range(4):
        for k in range(2, len(dx) + 1, 2):
            nx = dx[k] + pos[idx][0]
            ny = dy[k] + pos[idx][1]

            if 0 <= nx < n and 0 <= ny < n:
                if arr[nx][ny] > 0:
                    arr[pos[idx][0]][pos[idx][1]] += 1

    # step 5
    for x in range(n):
        for y in range(n):
            flag = False
            for idx in range(4):
                if pos[idx][0] == x and pos[idx][1] == y:
                    flag = True
                    break
            if flag:
                continue
            
            if arr[x][y] >= 2 and not visited[x][y]:
                arr[x][y] -= 2
                # clouds.append([x, y])
                

# arr = reduce(lambda x, y: x + y, arr, [])
# arr = [i for i in arr if i != 0]
    print(arr)
#  ←, ↖, ↑, ↗, →, ↘, ↓, ↙ 


# n, m = map(int, input().split())


# arr = [list(map(int, input().split())) for _ in range(n)]
# moves = []
# for i in range(m):
#     tmp = list(map(int, input().split()))
#     moves.append([tmp[0] - 1, tmp[1]])

# clouds = [[n-2, 0], [n-2, 1], [n-1, 0], [n-1, 1]]

# dx = [0, -1, -1, -1, 0, 1, 1, 1]
# dy = [-1, -1, 0, 1, 1, 1, 0, -1]
# for i in range(m):
#     # step 1.
#     # 이동
#     move = moves[i]
#     next_clouds = []
#     for cloud in clouds:
#         x = cloud[0]
#         y = cloud[1]
#         d = move[0]
#         s = move[1]
#         nx = (n + x + dx[d] * s) % n
#         ny = (n + y + dy[d] * s) % n
#         next_clouds.append([nx, ny])
    
#     # step 2.
#     visited = [[False]* n for _ in range(n)]
#     for cloud in next_clouds:
#         x = cloud[0]
#         y = cloud[1]
#         arr[x][y] += 1
#         visited[x][y] = True
    
#     # step 3
#     clouds = []

#     # step 4
#     cx = [-1, -1, 1, 1]
#     cy = [-1, 1, -1, 1]
#     for cloud in next_clouds:
#         x = cloud[0]
#         y = cloud[1]
#         count = 0
#         for i in range(4):
#             nx = x + cx[i]
#             ny = y + cy[i]

#             if 0 <= nx < n and 0<= ny < n and arr[nx][ny] >= 1:
#                 count += 1

#         arr[x][y] += count
        
#     # step 5

#     for i in range(n):
#         for j in range(n):
#             if arr[i][j] >= 2 and visited[i][j] == False:
#                 arr[i][j] -= 2
#                 clouds.append([i, j])
    
# ans = 0
# for i in range(n):
#     ans += sum(arr[i])


# print(ans)