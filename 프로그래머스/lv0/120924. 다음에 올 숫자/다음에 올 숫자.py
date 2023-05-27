# 1번 풀이
# def solution(common):
#     one, two, three = common[:3]
#     if two - one == three - two:
#         return common[-1] + three - two
#     else:
#         return common[-1] * (three // two)

def is_arithmetic_or_geometric(common):
    arithmetic_list, geometric_list = [], []
    
    for idx in range(len(common) - 1):
        arithmetic_list.append(common[idx + 1] - common[idx])
        geometric_list.append(common[idx + 1] / common[idx] if common[idx] else 0)
        
    if len(set(arithmetic_list)) == 1:
        return 1, arithmetic_list[-1]
    else:
        return 2, geometric_list[-1]
    
def get_next_number(last_num, diff_num, option):
    if option == 1:
        return last_num + diff_num
    elif option == 2:
        return last_num * diff_num

def solution(common):
    option, diff_num = is_arithmetic_or_geometric(common)
    
    return get_next_number(
            last_num=common[-1],
            diff_num=diff_num,            
            option=option
            )