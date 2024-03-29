# def solution(s):
#     answer = []

#     tmp = []
#     for idx, val in enumerate(s):
#         if val not in tmp:
#             tmp.append(val)
#             answer.append(-1)

#         elif val in tmp:
#             element = abs(idx - len(tmp) - tmp[::-1].index(val) - 1)
#             tmp.append(val)
#             answer.append(element)

#     return answer

def solution(s):
    answer = []

    dic = {}
    for idx, val in enumerate(s):
        if val not in dic:
            answer.append(-1)
        else:
            answer.append(idx - dic[val])

        dic[val] = idx

    return answer


print(solution("banana"))