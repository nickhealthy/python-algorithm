'''array의 각 element 중 divisor로 나누어 떨어지는 값을 오름차순으로 정렬한 배열을 반환하는 함수, solution을 작성해주세요.
divisor로 나누어 떨어지는 element가 하나도 없다면 배열에 -1을 담아 반환하세요.'''

arr = [3,2,6]


print(sorted(arr))
# 내 풀이
def solution(arr, divisor):
    ans = []
    for i in arr:
        if i % divisor == 0:
            ans.append(i)
    if ans[-1:] == []:
        ans = [-1]
    ans.sort()
    return ans


# 다른 사람 풀이
def solution1(arr, divisor): return sorted([i for i in arr if i % divisor == 0]) or [-1]