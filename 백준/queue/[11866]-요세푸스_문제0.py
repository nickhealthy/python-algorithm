n, k = map(int, input().split())
arr = [i for i in range(1, n + 1)]

index = 0
answer = []

for i in range(n):
    index %= (k - 1) % len(arr)
    answer.append(str(arr.pop(index)))

print(f'<{", ".join(answer)}>')