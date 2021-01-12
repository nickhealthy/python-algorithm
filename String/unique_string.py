# 1번 문자열에서 중복 글자 제거 후 다시 문자열로 치환
my_string = "aavvccccddddeee"

# 문자열을 set으로 변환
temp_set = set(my_string)

# join을 사용하여 set 내의 아이템을 연결
new_string = ''.join(temp_set)

print(new_string)

# outputs
# adevc


# 2번 isUnique or isNotunique
def unique(l):
    if len(l) == len(set(l)):
        print("All elements are unique")
    else:
        print("List has duplicates")


unique([1, 2, 3, 4])
# All elements are unique

unique([1, 1, 2, 3])
# List has duplicates
