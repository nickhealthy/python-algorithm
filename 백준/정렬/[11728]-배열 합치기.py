N, M = map(int, input().split())

listA = list(map(int, input().split()))
listB = list(map(int, input().split()))

print(*sorted(listA + listB))