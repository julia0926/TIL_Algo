def solution(today, terms, privacies):
    def make_total_days(piv_date, expire_month):
        pv, pm, pd = map(int, piv_date.split("."))
        pv -= 2000
        pm += expire_month
        pdays = (pv * 336) + (pm * 28) + pd
        return pdays
 
    today_days = make_total_days(today, 0)
    term_dic = dict(map(lambda x: (x.split()[0], int(x.split()[1])), terms))
    answer = []

    for index, privacy in enumerate(privacies):
        deadline, sort = privacy.split()
        expiry_month = term_dic[sort]
        privacy_days = make_total_days(deadline, expiry_month)
        diff_days = today_days - privacy_days
        if diff_days >= 0:
            answer.append(index+1)
        print(diff_days)
    return answer # 파기해야 할 개인정보 번호 오름차순
