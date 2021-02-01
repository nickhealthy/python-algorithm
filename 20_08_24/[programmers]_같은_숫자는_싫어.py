arr = [1, 1, 3, 3, 0, 1 ,1]

def solution(arr):
    ans = [arr[0]]
    for i in range(2, len(arr)):
        if arr[i] != arr[i-1]:
            ans.append(arr[i])
    return ans


