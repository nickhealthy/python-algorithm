def solution(arr):
    i = 0
    stk = []
    end = len(arr)

    while i < end:
        if not stk:
            stk.append(arr[i])
            i += 1

        if stk and stk[-1] < arr[i]:
            stk.append(arr[i])
            i += 1
        
        if i >= end:
            break

        if stk and stk[-1] >= arr[i]:
            stk.pop()

    return stk

print(solution([1, 4, 2, 5, 3]))