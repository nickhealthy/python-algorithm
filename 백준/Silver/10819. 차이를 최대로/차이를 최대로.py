from itertools import permutations

N = int(input())
arr = list(map(int, input().split()))

answer = 0
for permu_arr in list(permutations(arr)):
    mid_sum = 0
    for i in range(N - 1):
        mid_sum += abs(permu_arr[i] - permu_arr[i + 1])

    answer = max(answer, mid_sum)

print(answer)
