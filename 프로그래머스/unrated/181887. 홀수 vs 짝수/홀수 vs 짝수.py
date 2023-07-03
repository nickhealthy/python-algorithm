def solution(num_list):
    odd, even = 0, 0
    for idx, val in enumerate(num_list):
        if idx % 2 == 0:
            even += val
        else:
            odd += val
    return even if even > odd else odd