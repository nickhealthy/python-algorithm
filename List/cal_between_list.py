# list끼리의 연산
# set() 함수를 이용

def recursive_function():
    a = set()
    aTure = {i for i in range(1, 10001)}
    for i in range(1, 10001):
        for j in str(i):
            i += int(j)
        a.add(i)
    answer = sorted(aTure - a)

    for i in answer:
        print(i)


recursive_function()
