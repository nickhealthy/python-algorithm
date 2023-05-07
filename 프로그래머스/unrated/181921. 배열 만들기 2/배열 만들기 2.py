from collections import deque
# from time import time

def solution(l, r):
    answer = []
    
    for i in range(l, r + 1):
        if i % 5 == 0:
            tmp = ''
            for j in str(i):
                if j == '5' or j == '0':
                    tmp += j
                else:
                    break
            else:
                answer.append(int(tmp))
    
    return answer if answer else [-1]

print(solution(5, 555))

# # 다른 사람 풀이 1
# def solution(l, r):
#     answer = []
#     q = deque()
#     q.append('5')

#     while q:
#         now = q.popleft()
#         temp = int(now)
#         if l <= temp <= r: answer.append(temp)
#         else: break
#         q.append(now + '0')
#         q.append(now + '5')
    
#     return answer if answer else [-1]


# start_time = time()
# print(solution(5, 555))
# end_time = time()
# print(end_time - start_time)

# # 다른 사람 풀이 2
# def solution(l, r):
#     answer = []
    
#     for i in range(l, r + 1):
#         if not set(str(i)) - set(['0', '5']):
#             answer.append(i)

#     return answer


# start_time = time()
# print(solution(5, 555))
# end_time = time()
# print(end_time - start_time)

# # 다른 사람 풀이 3
# def solution(l, r):
#     answer = []
#     i = 1
#     n = 5

#     while True:
#         tmp = 5 * int(bin(i)[2:])
#         if l <= tmp <= r:
#             answer.append(tmp)
#         else:
#             break
        
#         i += 1

#     return answer if answer else [-1]


# start_time = time()
# print(solution(5, 555))
# end_time = time()
# print(end_time - start_time)


