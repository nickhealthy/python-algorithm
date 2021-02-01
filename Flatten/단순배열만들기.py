# recursive function 사용
# https://blog.naver.com/hankrah/221929249131 참고

def flatten(lst):
    result = []
    for item in lst:
        if type(item) == list:
            result += flatten(item)
        else:
            result += [item]
    return result


my_list = [[1, 2], [3, 4], [5, 6]]
print("원본: ", my_list)
print("변환: ", flatten(my_list))

my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("원본: ", my_list)
print("변환: ", flatten(my_list))
