def cal_final(stock, stock_count, each_money):
    return each_money + stock_count * stock


sungmin = junhyun = int(input())
stock_arr = list(map(int, input().split()))

sungmin_stock = 0
junhyun_stock = 0
up_stock, down_stock = 0, 0

for i in range(1, len(stock_arr)):
    # [준현이 전략]
    if junhyun >= stock_arr[i - 1]:
        junhyun_stock += junhyun // stock_arr[i - 1]
        junhyun -= stock_arr[i - 1] * (junhyun // stock_arr[i - 1])

    # [성민이 전략]
    # 전일 대비 하락
    if stock_arr[i - 1] > stock_arr[i]:
        down_stock += 1
        up_stock = 0

        # 전량 매수
        if down_stock >= 3:
            sungmin_stock += sungmin // stock_arr[i]
            sungmin -= stock_arr[i] * (sungmin // stock_arr[i])

    # 전일 대비 상승
    elif stock_arr[i - 1] < stock_arr[i]:
        up_stock += 1
        down_stock = 0

        # 전량 매도
        if up_stock >= 3 and sungmin_stock > 0:
            sungmin += stock_arr[i] * sungmin_stock
            sungmin_stock = 0

    # 가격이 동일할 때
    else:
        up_stock = 0
        down_stock = 0


junhyun = cal_final(stock_arr[-1], junhyun_stock, junhyun)
sungmin = cal_final(stock_arr[-1], sungmin_stock, sungmin)

if junhyun < sungmin:
    print("TIMING")
elif junhyun > sungmin:
    print("BNP")
else:
    print("SAMESAME")
