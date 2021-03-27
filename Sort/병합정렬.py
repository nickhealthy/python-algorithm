array = [7,5,9,0,3,1,6,2,4,8]

def quick_sort(arr, start, end):
    if start >= end:
        return 
    pivot = start
    left = start + 1
    right = end
    
    while left <= right:
        # 피벗보다 큰 데이터 찾기
        while left <= end and arr[left] <= arr[pivot]:
            left += 1
        # 피벗보다 작은 데이터 찾기
        while right > start and arr[right] >= arr[pivot]:
            right -= 1
        # 엇갈리는 상황이 온다면 기존 피벗이랑 교환 - 분할
        if left > right:
            arr[right], arr[pivot] = arr[pivot], arr[right]
        # 아니라면 데이터 교환
        else:
            arr[left], arr[right] = arr[right], arr[left]

    quick_sort(arr, start, right - 1)
    quick_sort(arr, right + 1, end)

quick_sort(array, 0, len(array) - 1)
print(array)