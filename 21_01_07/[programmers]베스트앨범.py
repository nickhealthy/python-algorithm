def solution(genres, plays):
    di = {}

    for idx, genre in enumerate(genres):
        if genre not in di.keys():
            di[genre] = [(idx, plays[idx])]
        else:
            di[genre].append((idx, plays[idx]))

    for i in di.keys():
        di[i].sort(key=lambda x : x[1], reverse=True)


    sorted_di= sorted(list(di.values()), key=lambda x : sum(x2[1] for x2 in x), reverse=True)

    answer = []
    
    for i in sorted_di:
        for j in i[:2]:
            answer.append(j[0])
            
    return answer