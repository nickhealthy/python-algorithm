# 사회자가 불러주는 배열[x][y]를 0으로 만든다.
# 가로, 세로 체크는 루프를 돌면서 체크한다.
#   - ex) arr[x][0] == 0 ~ arr[x][4] == 0 체크
#   - ex) arr[0][y] == 0 ~ arr[4][y] == 0 체크
# 대각선은 좌표 값을 가진 배열을 만들어 두고 해당 경로들이 모두 0인지 체크한다.

# 첫 번째 배열은 왼쪽 위에서 오른쪽 아래 대각선 각 ele은(x, y) 값
# 두 번째 배열은 오른쪽 위에서 왼쪽 아래 대각선 각 ele은(x, y) 값

bingo_maps = []
for _ in range(5):
    bingo_maps.append(list(map(int, input().split())))


num_maps = []
for _ in range(5):
    num_maps.append(list(map(int, input().split())))

num_maps = sum(num_maps, [])

cross_arrs = [
    [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)],
    [(0, 4), (1, 3), (2, 2), (3, 1), (4, 0)]
]


def solution():
    answer = 0

    for num in num_maps:
        answer += 1
        flag = False
        for i in range(5):
            for j in range(5):
                if bingo_maps[i][j] == num:
                    bingo_maps[i][j] = 0
                    flag = True
                    break
            if flag:
                break

        # 빙고 3줄 이상 체크
        # 가로줄 체크
        line = 0
        for x in range(5):
            for y in range(5):
                if bingo_maps[x][y] != 0:
                    break
            # 한 루프를 정상적으로 돌았으면 해당 가로줄은 빙고줄
            else:
                line += 1

                if line >= 3:
                    return answer

        # 세로줄 체크
        for x in range(5):
            for y in range(5):
                if bingo_maps[y][x] != 0:
                    break
            else:
                line += 1

                if line >= 3:
                    return answer

        # 대각선 체크
        for cross_arr in cross_arrs:
            for x, y in cross_arr:
                if bingo_maps[x][y] != 0:
                    break

            else:
                line += 1

                if line >= 3:
                    return answer


print(solution())
