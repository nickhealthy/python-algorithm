def solution(n, slicer, num_list):
    answer = []
    
    a, b, c = slicer
    if n == 4:
        return num_list[a:b+1:c]
    elif n == 3:
        return num_list[a:b+1]
    elif n == 2:
        return num_list[a:]
    else:
        return num_list[:b+1]
    
    return -1