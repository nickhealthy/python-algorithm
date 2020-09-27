'''
A = ['a','b','b','c']
B = ['a','b','c']

# dic 형으로 고유한 키값과 값을 0으로 초기화
dic1 = {i : 0 for i in A}
print(len(dic1.keys()), dic1.keys())

# a, b, b, c
for i in A:
    # a, b, c
    for j in dic1.keys():
        if i == j:
            dic1[i] += 1
print(dic1)

# a, b, c
for i in B:
    # a, b, c
    for j in dic1.keys():
        if i == j:
            dic1[i] -= 1
print(dic1)

for i in dic1.keys():
    if dic1[i] > 0:
        print(i)

'''

# 차집합은 중복된 선수의 이름이 있으므로 사용 불가
# 정렬을 한 후 zip 함수로 남는 하나의 값을 출력
PAR = ['leo', 'kiki', 'eden']
COM = ['eden', 'kiki']

def solution(participant, completion):
    participant.sort()
    completion.sort()

    for par, com in zip(participant, completion):
        if par != com:
            return par

    return participant[-1] 