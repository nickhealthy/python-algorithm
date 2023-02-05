import sys

input = sys.stdin.readline

N = input().strip()
if '0x' in N:
    print(int(N, 16))
elif '0' == N[0]:
    print(int(N, 8))
else:
    print(int(N))