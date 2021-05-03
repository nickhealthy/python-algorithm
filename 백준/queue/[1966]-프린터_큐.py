test_cases = int(input())

for _ in range(test_cases):
    n, m = map(int, input().split())
    imp = list(map(int, input().split()))
    imp_idx = list(range(n))
    imp_idx[m] = "target"

    count = 0

    while True:
        # 첫 번째 값이 가장 '중요도'가 높은 것이면
        if imp[0] == max(imp):
            count += 1
            # 첫 번째 값이 'target'이라면
            if imp_idx[0] == "target":
                print(count)
                break
            else:
                imp.pop(0)
                imp_idx.pop(0)
        else:
            imp.append(imp.pop(0))
            imp_idx.append(imp_idx.pop(0))
