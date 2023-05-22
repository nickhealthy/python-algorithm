def solution(todo_list, finished):
    answer =[]
    for todo, isTrue in zip(todo_list, finished):
        if not isTrue:
            answer.append(todo)
    return answer