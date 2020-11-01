import random

# def findMinIdx(ary):
#     retIdx = 0
#     for i in range(len(ary)):
#         if (ary[retIdx] < ary[i]):
#             retIdx = i
#     return retIdx


## 함수 선언부
def insertionSort(ary):
    def findMinIdx(ary):
        retIdx = 0
        for i in range(len(ary)):
            if (ary[retIdx] < ary[i]):
                retIdx = i
        return retIdx

    newAry = []
    for i in range(len(ary)):
        minIdx = findMinIdx(ary)
        newAry.append(ary[minIdx])
        del (ary[minIdx])
    return newAry


## 전역 변수부
before = [random.randint(10, 99) for _ in range(20)]
after = []
## 메인 코드부
print('정렬전-->', before)
after = insertionSort(before)  # 내림차순
print('정렬후-->', after)
