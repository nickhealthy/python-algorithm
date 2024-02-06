N, M = map(int, input().split())

lstA = list(map(int, input().split()))
lstB = list(map(int, input().split()))

print(*sorted(lstA + lstB))