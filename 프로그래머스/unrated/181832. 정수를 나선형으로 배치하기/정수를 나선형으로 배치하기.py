dx = (0, 1, 0, -1)
dy = (1, 0, -1, 0)


def solution(n):
    now = 2
    answer = [[0] * n for _ in range(n)]
    answer[0][0] = 1

    x, y = 0, 0
    i = 0
    while now <= n * n:
        nx, ny = x + dx[i], y + dy[i]
        if not (0 <= nx < n and 0 <= ny < n) or answer[nx][ny]:
            i += 1
            i %= 4
            continue

        x, y = nx, ny
        answer[x][y] = now
        now += 1

    return answer