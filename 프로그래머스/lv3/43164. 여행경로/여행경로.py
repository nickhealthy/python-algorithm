def solution(tickets):
    routes = {}
    stack = ['ICN']
    path = []
    
    for start, end in tickets:
        routes[start] = routes.get(start, []) + [end]
        
    for key in routes.keys():
        routes[key].sort(reverse=True)
    
    while len(stack) > 0:
        top = stack[-1]
        if top not in routes or len(routes[top]) == 0:
            path.append(stack.pop())
        
        else:
            stack.append(routes[top].pop())
        
        
    return path[::-1]