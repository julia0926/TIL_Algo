from datetime import datetime
def solution(today, terms, privacies):
    now_year, now_month, now_day = map(int, [today[:4], today[5:7], today[-2:]])
    term_dic = {}
    for t in terms:
        sort, valid_date = t.split()
        term_dic[sort] = int(valid_date)
    
    def calculate_date(date, type):
        p_year, p_month, p_day = map(int, date.split('.'))
        p_month += term_dic[type]
        if p_month > 12:
            p_year += 1
            p_month -= term_dic[type]+1
        p_day -= 1
        if p_day == 0:
            p_day = 28
        return p_year, p_month, p_day

    #현재보다 이후인지 확인 
    def validate_date(y, m, d):
        compare_date = datetime(y, m, d)
        now_date = datetime(now_year, now_month, now_day)
        return True if compare_date >= now_date else False

    result = []
    for idx, p in enumerate(privacies):
        date, type = p.split()
        y, m, d = calculate_date(date, type)
        if not validate_date(y, m, d): #보관 가능하다면
            result.append(idx+1)

    return result


solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"])