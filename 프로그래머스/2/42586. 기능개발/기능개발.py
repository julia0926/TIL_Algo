def solution(progresses, speeds):
    answer = []
    days = []
    for progress, speed in zip(progresses, speeds):
        day = (100 - progress) // speed
        remain = (100 - progress) % speed
        if remain != 0:
            day += 1
        days.append(day)
    
    cnt = 1
    piv = days[0]
    for day in days[1:]:
        if piv < day:
            answer.append(cnt)
            cnt = 1
            piv = day
        else:
            cnt += 1
    answer.append(cnt)
    return answer