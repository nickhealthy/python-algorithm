N = int(input())
W = list(map(int, input().split()))

a = sorted(W)
_a = sorted(W, reverse=True)

answer = []
for a1, a2 in zip(a, _a):
    answer.append(a1 + a2)

print(min(answer))