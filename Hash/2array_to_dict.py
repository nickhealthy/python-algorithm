# iterable한 객체들을 dict()의 key와 values 값들로 바꿔줌
# 2차원 배열에서 각각의 "카테고리"를 나눠야 할 때 유용함


def solution(clothes):
    di = dict()

    for cloth in clothes:
        if cloth[1] not in di.keys():
            di[cloth[1]] = [cloth[0]]
        else:
            di[cloth[1]].append(cloth[0])

    return di
