def solution(str_list):
    answer = []
    
    for i in range(len(str_list)):
        if str_list[i] == 'l':
            return str_list[:i] if str_list[:i] else []
        elif str_list[i] == 'r':
            return str_list[i + 1:] if str_list[i + 1:] else []
                
    
    return []