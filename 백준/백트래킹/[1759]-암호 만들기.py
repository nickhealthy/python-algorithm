from itertools import combinations

l, c = map(int, input().split()) # 암호 길이, 주어지는 문자 개수
arr = sorted(input().split())

vowels = ['a', 'e', 'i', 'o', 'u']
comb = combinations(arr, l)

for c in comb:
    count = 0
    for letter in c:
        if letter in vowels:
            count += 1
    
    if (count >= 1) and (count <= l - 2):
        print(''.join(c))
