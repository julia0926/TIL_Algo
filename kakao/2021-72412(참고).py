
from itertools import combinations
from bisect import bisect_left


def all_cases(temp):
    cases = []
    for k in range(5):
        for li in combinations([0,1,2,3], k):
            case = ''
            for idx in range(4):
                if idx not in li:
                    case += temp[idx]
                else:
                    case += '-'
            cases.append(case)
    return cases

def solution(info, query):
    answer = []
    all_people = {}
    for i in info:
        split_info = i.split() 
        cases = all_cases(i.split()) #한 지원자의 16가지 모든 경우의 수를 계산 
        for case in cases:
            if case not in all_people: #해당 케이스가 없으면 
                all_people[case] = [int(split_info[4])] #해당 케이스를 키값으로 value 값에 넣음
            else: #이미 들어있으면
                all_people[case].append(int(split_info[4])) #추가로 해당 케이스의 점수값 넣음 
    
    for key in all_people.keys(): 
        all_people[key].sort() #지원자들의 점수값으로 오름차순 
    
    for q in query:
        split_q = q.split()
        target = split_q[0] + split_q[2] + split_q[4] + split_q[6] #면접자가 요구하는 정보들 
        if target in all_people.keys(): #지원자 정보중에 면접자가 원한 정보가 있으면 
            answer.append(len(all_people[target]) - bisect_left(all_people[target], int(split_q[7]), lo=0, hi=len(all_people[target])))
            #해당 점수가 되는 지원자들의 수 - 
        else:
            answer.append(0)
    # 면접자가 요구한 조건에 맞는 지원자들의 점수 - 면접자가 요구한 점수에 해당하는 값 이상인 명수를 구하기 위해 인덱스 리턴 (이진탐색 !! )
    # [150]
    # [150, 210]
    # [260]
    # [50, 260]
    # [50, 80, 150, 210]
    # [50, 80, 150, 150, 210, 260]


print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],
["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))