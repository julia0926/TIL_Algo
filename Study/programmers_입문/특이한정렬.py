#https://school.programmers.co.kr/learn/courses/30/lessons/120880
def solution(numlist, n):
    arr = list(map(lambda x: abs(n-x), numlist))
    dic = {}
    for i in range(len(numlist)):
        dic[numlist[i]] = arr[i]
    tt = sorted(dic.items(), key = lambda x: (x[1], -x[0]))
    answer = []
    for i in tt:
        answer.append(i[0])
    return answer


def solution2(numlist, n):
    arr = sorted(numlist, key = lambda x: (abs(x-n), n-x)) 
    return arr

solution([10000,20,36,47,40,6,10,7000]	, 30)
solution2([10000,20,36,47,40,6,10,7000]	, 30)