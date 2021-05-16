n = int(input())
arr = [True for _ in range(1000001)]
my_list = []
for i in range(2, int(len(arr) ** 0.5) + 1):
    if arr[i] == True:
        my_list.append(i)
        for j in range(i * 2, len(arr), i):
            arr[j] = False

answer = 0
for i in range(n, len(arr)):
    if i == 1:
        continue
    # 소수 팰린드롬 판별
    if str(i) == str(i)[::-1] and arr[i]:
        answer = i
        break

# n의 범위(백만)에서 안나올 떈 100만 이후의 가장 큰 소수값 출력
if answer == 0:
    print(1003001)
else:
    print(answer)