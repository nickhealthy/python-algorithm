# def solution(l, r):
#     answer = []
    
#     for i in range(l, r + 1):
#         if i % 5 == 0:
#             tmp = ''
#             for j in str(i):
#                 if j == '5' or j == '0':
#                     tmp += j
#                 else:
#                     break
#             else:
#                 answer.append(int(tmp))
    
#     return answer if answer else [-1]

# print(solution(5, 555))

def solution(l, r):
    answer = []
    
    for i in range(l, r + 1):
        if not set(str(i)) - set(['0', '5']):
            answer.append(i)

    return answer if answer else [-1]