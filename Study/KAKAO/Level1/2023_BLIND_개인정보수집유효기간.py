# 년월일로 계산하는 것이 아닌 day로 다 계산해서 풀어서 구해야함 

def solution(today, terms, privacies):
    now_year, now_month, now_day = map(int, [today[:4], today[5:7], today[-2:]])
    term_dic = {}
    for t in terms:
        sort, valid_date = t.split()
        term_dic[sort] = int(valid_date)      

    def today_cal(date):
        p_year, p_month, p_day = map(int, date.split('.'))
        return ((p_year-2000) * 12 * 28) + p_month * 28 + p_day

    result = []
    today_diff = today_cal(today)
    for idx, p in enumerate(privacies):
        date, type = p.split()
        if today_cal(date) + term_dic[type]*28 <= today_diff:
            result.append(idx+1)

    return result

# print(solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2020.01.28 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))
print(solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))
print(solution("2020.01.01", ["Z 3", "D 5"], ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]))