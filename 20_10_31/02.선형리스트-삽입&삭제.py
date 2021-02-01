katok = ['다현', '정연', '쯔위', '사나', '지효']


def insert_data(position, friend):
    katok.append(None)  # 빈칸 추가
    kLen = len(katok)

    for i in range(kLen - 1, position, -1):
        katok[i] = katok[i - 1]
        katok[i - 1] = None

    katok[position] = friend


def delete_data(position):
    kLen = len(katok)
    katok[position] = None

    for i in range(position + 1, kLen):
        katok[i - 1] = katok[i]
        katok[i] = None

    del (katok[kLen - 1])


insert_data(2, '솔라')
print(katok)
insert_data(5, '재남')
print(katok)

delete_data(5)
print(katok)