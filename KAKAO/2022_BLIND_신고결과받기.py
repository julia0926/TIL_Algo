# https://programmers.co.kr/learn/courses/30/lessons/92334

def solution(id_list, report, k):
    reporter_dic = {id: [] for id in id_list}
    #id값에 따른 배열 넣을 때 사용 
    result = [0] * len(id_list)
    for value in set(report):
        reporter, reported = value.split()
        reporter_dic[reported].append(reporter)

    for key, value in reporter_dic.items():
        if len(value) >= k:
            for j in value:
                result[id_list.index(j)] += 1
    return result

   

solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2)
solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3)