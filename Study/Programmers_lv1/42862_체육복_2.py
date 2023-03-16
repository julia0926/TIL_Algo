def solution(n, lost, reserve):
    set_reserve = set(reserve) - set(lost) #여분있지만 잃어버리지 않음
    set_lost = set(lost) - set(reserve)
    for value in set_reserve: #여분이 있는 학생들 
        if value - 1 in set_lost:
            set_lost.remove(value-1) #지워저버렸으면, ,,
        elif value + 1 in set_lost:
            set_lost.remove(value+1)
    return n - len(set_lost)
