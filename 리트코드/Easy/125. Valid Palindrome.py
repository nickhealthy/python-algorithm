s = "A man, a plan, a canal: Panama"


# 첫 번째 풀이
def valid_is_palind_room(s: str) -> bool:
    strs = []
    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    # 팰린드룸 여부 판별
    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False

    return True


print(valid_is_palind_room(s))
