def solution(num): 
    num = list(map(str, num))
    # print(num)
    num.sort(key = lambda x: x * 3, reverse = True) # 666, 222, 101010
    # print(num)
    return str(int(''.join(num)))


# from itertools import permutations


# def solution(numbers):
#     answer = '0'
#     permu = list(permutations(numbers, len(numbers)))

#     for num in permu:
#         num_str = ''.join(map(str, num))

#         if answer < num_str:
#             answer = num_str

#     return answer

# def solution(numbers):
#     answer = ''
#     numbers = [str(x) for x in numbers]
#     numbers.sort(key=lambda x: (x * 4)[:4], reverse=True)
    
#     answer = ''.join(numbers)
    
#     if answer[0] == '0':
#         answer = '0'
        
#     return answer
    