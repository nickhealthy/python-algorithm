def solution(a, b, c, d):
    count = {}
    for x in (a, b, c, d):
        count[x] = count.get(x, 0) + 1

    count_list = sorted(count.items(), key=lambda x: x[1])

    if len(count_list) == 1:
        return count_list[0][0] * 1111
    elif len(count_list) == 2:
        p, c = count_list.pop()
        q = count_list[0][0]
        if c == 3:
            return (10 * p + q) ** 2
        else:
            return (p + q) * abs(p - q)
    elif len(count_list) == 3:
        return count_list[0][0] * count_list[1][0]
    else:
        return min(a, b, c, d)


print(solution(6,3,3,6))