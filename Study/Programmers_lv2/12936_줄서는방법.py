#https://school.programmers.co.kr/learn/courses/30/lessons/131701
def solution(elements):    
    leng = len(elements)
    result = set()
    #elements = elements * 2 #인덱스 상관없이 그냥 두배로 늘릴 수도 있네 ?!
    for i in range(leng):
        for j in range(leng):
            end = j+i+1
            if end > leng: 
                #앞뒤부분 나눠서 더해줘야함 
                result.add(sum(elements[j:] + elements[:end-leng]))
            else:
                result.add(sum(elements[j:end]))
    return len(result)

solution([7,9,1,1,4])