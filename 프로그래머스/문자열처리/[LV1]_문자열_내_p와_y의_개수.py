def solution(s):
    p_count = 0
    y_count = 0

    for i in s:
        if i.lower() == 'p':
            p_count += 1
        elif i.lower() == 'y':
            y_count += 1
    
    return True if p_count == y_count else False