from collections import Counter

# def solution(line):
#     tmp = ""
#     for key, count in Counter(line).items():
#         if count > 1:
#             tmp += key+"*"
#         else:
#             tmp += key
#         # print(key, count)
#     print(tmp)
#     return tmp

def solution(line):
    tmp = line[0]
    for i in range(1, len(line)):
        print(line[i-1], line[i], tmp)
        if line[i-1] == line[i]:
            if tmp[-1] == "*":
                continue
            tmp += "*"
        else:
            tmp += line[i]
    return tmp
    
solution("aabbbc")
