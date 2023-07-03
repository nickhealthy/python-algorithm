def solution(arr):
    answer = 1

    pre_arr = []
    while True:
        count = 1
        # pre_arr = arr
        for i in range(len(arr)):
            if arr[i] >= 50 and arr[i] % 2 == 0:
                arr[i] //= 2
                count = 0
            elif arr[i] < 50 and arr[i] % 2:
                arr[i] = arr[i] * 2 + 1
                count = 0
            
        if count:
            break

        answer += 1

    return answer - 1