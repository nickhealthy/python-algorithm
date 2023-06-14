# def solution(participant, completion):
#     participant.sort()
#     completion.sort()

#     for i, z in zip(participant, completion):
#         if i != z:
#             return i
#     return participant[-1]

# from collections import Counter

# def solution(participant, completion):
#     return ''.join(Counter(participant) - Counter(completion))


def solution(participant, completion):
    d = {}
    for i in participant:
        d[i] = d.get(i, 0) + 1
    
    for i in completion:
        d[i] -= 1 
        
    dnf = [k for k, v in d.items() if v > 0]
    
    return dnf[0]
    