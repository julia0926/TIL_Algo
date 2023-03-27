def solution(record):
    answer = []
    state = []
    dic = {}
    for r in record:
        info = r.split()
        if info[0] == 'Enter' or info[0] == "Change":
            dic[info[1]] = info[2]
            if info[0] == "Enter":
                state.append((info[0], info[1]))
        elif info[0] == "Leave":
            state.append((info[0], info[1]))
            
    for s, i in state:
        if s == "Enter":
            answer.append(dic[i]+"님이 들어왔습니다.")
        else:
            answer.append(dic[i]+"님이 나갔습니다.")
    # print(answer)
    return answer