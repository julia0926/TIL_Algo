from collections import defaultdict

def solution(keymap, targets):
    dic = defaultdict(int)
    for key in keymap:
        for i in range(len(key)):
            if dic[key[i]] == 0:
                dic[key[i]] = i+1
            else:
                dic[key[i]] = min(i+1,dic[key[i]])

    answer = []
    for target in targets:
        value = 0
        for t in target:
            if t in dic.keys():
                value += dic[t]
            else:
                value = -1
                break
            # print(dic[t])

        answer.append(value)

    # print(answer)
    return answer