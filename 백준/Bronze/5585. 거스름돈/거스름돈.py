import sys

input = sys.stdin.readline
n = int(input())

coins = [500, 100, 50, 10, 5, 1]
change = 1000 - n

answer = 0
for coin in coins:
    while change // coin:
        answer += (change // coin)
        change = change - coin * (change // coin)

print(answer)
