arr = []
flag = False
for i in range(9):
    n = int(input())
    arr.append(n)

arr.sort()
cnt = sum(arr)
tmp = []
for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if cnt - (arr[i] + arr[j]) == 100:
            tmp.append([arr[i], arr[j]])
            flag = True
            break
    if flag:
        break

for i in range(len(arr)):
    if arr[i] not in tmp[0]:
        print(arr[i])