def solution(number, k):
    stack = [number[0]]
    for num in number[1:]:
        while stack and num > stack[-1] and k > 0:
            stack.pop()
            k -= 1
        stack.append(num)
        
    while k > 0:
        stack.pop()
        k -= 1
    
    return ''.join(stack)