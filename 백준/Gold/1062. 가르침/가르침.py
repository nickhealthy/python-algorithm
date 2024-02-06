import sys
from itertools import combinations

input = sys.stdin.readline

N, K = map(int, input().split())


def word2bit(word):
    bit = 0
    for char in word:
        bit = bit | (1 << ord(char) - ord("a"))

    return bit


words = [input().rstrip() for _ in range(N)]
bits = list(map(word2bit, words))
base_bit = word2bit("acint")

if K < 5:
    print(0)
else:
    answer = 0

    alphabet = [1 << i for i in range(26) if not (base_bit & 1 << i)]
    for combination in combinations(alphabet, K - 5):
        know_bit = sum(combination) | base_bit

        count = 0
        for bit in bits:
            if know_bit & bit == bit:
                count += 1

        answer = max(answer, count)

    print(answer)
