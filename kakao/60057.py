def solution(s):
    answer = 10000
    nlist = []
    for k in range(1,len(s)//2+1):
        for i in range(0,len(s)-1,k):
            nlist.append(s[i:i+k])
        #print(nlist)
        res = ''
        cnt = 1
        first = nlist[0]
        #print(first)
        for j in range(1,len(nlist)):
            if nlist[j] == first:
                cnt += 1
                first = nlist[j]
                if j == len(nlist)-1:
                    res += str(cnt)+first
            else:
                if j == len(nlist)-1:
                    res += first
                if cnt == 1:
                    res += first
                if cnt > 1:
                    res += str(cnt)+first
                first = nlist[j]
                cnt = 1
            print(res)
        nlist = []
        answer = min(answer,len(res))
    return answer

print(solution("abcabcdede"))