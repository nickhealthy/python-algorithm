countA, countB = map(int, input().split())

A = set(map(int, input().split()))
B = set(map(int, input().split()))


# [오답] print((len(A) - len(B)) + (len(B) - len(A)))
# 차집합이 아닌 set 자료형의 개수만큼 빼기를 하므로 답이 틀리게 나옴 
# 문제에서 요구하는 대칭 차집합을 구하기 위해선 집합끼리의 뺄셈을 해야함

print(len(A - B) + len(B - A))