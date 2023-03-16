'''
k개 팔려면 최소 몇분 ?
N = 빵의 개수
'''

def change_to_minute(time):
    hour, minute = map(int, time.split(":"))
    hour *= 60
    return hour + minute

def solution(bakery_schedule, current_time, k):
    answer = -1
    bread_dic = {}

    for info in bakery_schedule:
        time, bread = info.split()
        print(time, bread)
        bread_dic[change_to_minute(time)] = int(bread)

    current_minute = change_to_minute(current_time)
    sale_bread_count = 0
    
    for bread_minute in bread_dic.keys():
        if current_minute <= bread_minute:
            sale_bread_count += bread_dic[bread_minute]
        if sale_bread_count >= k:
            return bread_minute - current_minute

    return answer

print(solution(["12:20 5", "09:05 10", "13:25 6", "14:24 5"], "12:05", 10))
print(solution(["12:00 10"], "12:00", 11))