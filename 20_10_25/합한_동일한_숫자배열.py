# arr = [1, 2, 3, 4, 6]
# arr = [1, 2, 3, 3]
# arr = [1, 2, 1]
arr = [2, 3, 4, 7]


def balancedSum(arr):
    tmp = 0
    ano_tmp = arr[-1]
    for i in range(len(arr)):
        tmp += arr[i]

    for i in range(len(arr)):
        if ano_tmp > tmp:
            pass
        else:
            ano_tmp += arr[-i - 1]

    if tmp == ano_tmp:
        return arr[i]


print(balancedSum(arr))