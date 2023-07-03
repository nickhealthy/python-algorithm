def solution(my_string: str, indices: list) -> str:
    my_string = list(my_string)

    cnt = 0
    for i in sorted(indices):
        del my_string[i + cnt]
        cnt -= 1

    return ''.join(my_string)