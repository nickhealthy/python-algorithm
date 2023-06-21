N, S, R = map(int, input().split())
broken_list = list(map(int, input().split()))
recover_list = list(map(int, input().split()))

kayak = [1] * (N + 2)
for num in broken_list:
    kayak[num] -= 1

for num in recover_list:
    kayak[num] += 1

for i in range(1, N + 1):
    if kayak[i - 1] == 0 and kayak[i] == 2:
        kayak[i - 1:i + 1] = [1, 1]
    elif kayak[i + 1] == 0 and kayak[i] == 2:
        kayak[i:i + 2] = [1, 1]

print(kayak.count(0))