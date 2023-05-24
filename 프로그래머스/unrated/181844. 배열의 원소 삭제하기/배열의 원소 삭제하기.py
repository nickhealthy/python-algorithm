def solution(arr, delete_list):
    answer = []
    for i in range(len(delete_list)):
        while delete_list[i] in arr:
            arr.remove(delete_list[i])
            
    return arr