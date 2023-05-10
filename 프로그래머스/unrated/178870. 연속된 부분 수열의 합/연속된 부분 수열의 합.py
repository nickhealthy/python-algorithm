def solution(sequence, k):
    answer = []

    score = 0
    left, right = 0, -1
    end = len(sequence)
    
    while True:
        if score == k:
            answer.append([left, right])

        if score < k:
            right += 1
            if right >= end:
                break
            score += sequence[right]
        
        else:
            score -= sequence[left]
            left += 1
            if left >= end:
                break
    
    answer.sort(key=lambda x: (x[1] - x[0], x[0]))
    return answer[0]

print(solution([1, 2, 3, 4, 5], 7))