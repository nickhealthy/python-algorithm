def solution(s):
    lst = [0] + list(s)
    
    if lst[-1] == '(' or lst.count('(') != lst.count(')'):
        return False
    
    stack = []
    while len(lst) != 1:
        try:
            if lst.pop() == ')':
                stack.append(')')        
            else:
                stack.pop()
        except:
            return False

    return True
