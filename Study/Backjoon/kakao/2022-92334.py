def solution(id_list, report, k):
    set_report = set(report)
    reporter_dic = {id: set() for id in id_list} #신고 한 사람 
    reported_dic = {id: 0 for id in id_list} #신고 당한 사람 
    for i in set_report:
        a, b = i.split()
        reported_dic[b] += 1
        reporter_dic[a].add(b)
    arr = []
    for key, val in reported_dic.items():
        if val == k:
            arr.append(key)
    arr = set(arr)
    result = []
    for key, val in reporter_dic.items():
        result.append(len(val & arr))
    return result
    

print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))
# print(solution(["con", "ryan"],["ryan con", "ryan con", "ryan con", "ryan con"], 3 ))