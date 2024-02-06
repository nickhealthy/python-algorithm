N, M = map(int, input().split())
CARDS = list(map(int, input().split()))

CARDS.sort()

result = 0
for i in range(N - 2):
    for j in range(i+1, N - 1):
        for k in range(j+1, N):
            if CARDS[i] + CARDS[j] + CARDS[k] > M:
                continue
            else:
                result = max(result, CARDS[i]+CARDS[j]+CARDS[k])

print(result)