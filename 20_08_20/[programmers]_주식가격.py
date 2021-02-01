def solution(prices):
    answer = []

    for i in range(0, len(prices)-1):
        fin = False
        for j in range(i+1, len(prices)):
            if prices[i] > prices[j]:
                answer.append(j-i)
                fin = True
                break
        if fin == False:
            answer.append(len(prices)-i-1)

    answer.append(0)

    return answer