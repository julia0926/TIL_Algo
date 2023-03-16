from collections import defaultdict
import math

def time_calculate(out_time, in_time):
    out_hour, out_min = map(int, out_time.split(':'))
    in_hour, in_min = map(int, in_time.split(':'))
    if out_hour == in_hour: #시간이 같다면
        return out_min - in_min
    else:
        return ((out_hour - in_hour) * 60) + out_min - in_min


def solution(fees, records):
    info = defaultdict(str)
    carfee_list = defaultdict(int)
    answer = []
    for recode in records:
        time, car_num, state = recode.split()
        if car_num in info.keys() and state == 'OUT': #포함되어 있다면 ? 시간 계산해서 누적값 구해야함 
            print(car_num, time, '-', info[car_num][0])
            accumulate_time = time_calculate(time, info[car_num][0])
            if car_num in carfee_list.keys(): #이미 계산된 주차요금이 있따면 누적해야함
                carfee_list[car_num] += accumulate_time
            else:
                carfee_list[car_num] = accumulate_time

        info[car_num] = [time, state]
    
    for key, value in info.items():
        if value[1] == 'IN': #출차 내역이 없는거
            accumulate_time = time_calculate("23:59", value[0])
            print(carfee_list[key], accumulate_time)
            carfee_list[key] += accumulate_time
        if carfee_list[key] > fees[0]: #기본요금 넘으면 
            print(math.ceil((carfee_list[key] - fees[0])/fees[2]) * 600 + fees[1])
            carfee_list[key] = fees[1] + (math.ceil((carfee_list[key] - fees[0])/fees[2]) * fees[3])
        else:
            carfee_list[key] = fees[1]
    tmp = sorted(carfee_list.items(), key=lambda x: x[0])
    for t in tmp:
        answer.append(t[1])
    # print(answer)
    return answer

solution([1, 461, 1, 10], ["00:00 1234 IN"])
# solution([180, 5000, 10, 600],
# ["05:34 5961 IN", 
# "06:00 0000 IN", 
# "06:34 0000 OUT", 
# "07:59 5961 OUT", 
# "07:59 0148 IN", 
# "18:59 0000 IN", 
# "19:09 0148 OUT", 
# "22:59 5961 IN", 
# "23:00 5961 OUT"])