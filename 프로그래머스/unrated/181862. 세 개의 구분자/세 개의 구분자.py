def solution(myStr):
    answer = ''

    for i in myStr:
        if i == 'a' or i == 'b' or i == 'c':
            answer += ' '
            continue

        answer += i

    return answer.split() if answer.split() else ["EMPTY"]