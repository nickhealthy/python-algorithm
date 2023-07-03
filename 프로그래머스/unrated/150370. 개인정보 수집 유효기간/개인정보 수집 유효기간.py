# def solution(today, terms, privacies):
#     answer = []

#     terms_dict = {}
#     for term in terms:
#         terms_type, terms_period = term.split()
#         terms_dict[terms_type] = int(terms_period)

#     i = 1
#     for privacie in privacies:
#         pri_date, pri_type = privacie.split()
#         year, month, day = map(int, pri_date.split('.'))

#         yy, mm = divmod(terms_dict[pri_type], 12)

#         if month + mm > 12:
#             yy += 1
#             month = mm + month - 12

#             if day == 1:
#                 day = 28
#                 if month == 1:
#                     month = 12
#                     year -= 1
#                 else:
#                     month -= 1
#             else:
#                 day -= 1

#             str_month = str(month)
#             str_day = str(day)

#         else:
#             if day == 1:
#                 day = 28
#                 if month == 1:
#                     month = 12
#                     year -= 1
#                 else:
#                     month -= 1
#             else:
#                 day -= 1

#             str_month = str(month + mm)
#             str_day = str(day)

#         if len(str_month) == 1:
#             str_month = '0' + str_month
#         if len(str_day) == 1:
#             str_day = '0' + str_day

#         result = '.'.join((str(year + yy), str_month, str_day))
#         print(result)
#         if result < today:
#             answer.append(i)

#         i += 1

#     return answer

def cal_date(date):
    year, month, day = map(int, date.split('.'))
    return year * 28 * 12 + month * 28 + day


def solution(today, terms, privacies):
    months = {v[0]: int(v[2:]) * 28 for v in terms}
    today = cal_date(today)

    expire = [
        i + 1 for i, val in enumerate(privacies)
        if cal_date(val[:-2]) + months[val[-1]] <= today
    ]

    return expire