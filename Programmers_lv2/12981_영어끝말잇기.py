#https://school.programmers.co.kr/learn/courses/30/lessons/12981

def solution(n, words):
    #결과 : 탈락사람 번호, 자신의 몇번째 차례에서 탈락 !
    say_word = [] #말한 단어들 누적
    for idx in range(len(words)-1): 
        #현재단어의 끝과 다음 단어의 시작이 다르고 or 다음 단어중에 말한 단어가 있다면
        if words[idx][-1] !=  words[idx+1][0] or words[idx+1] in say_word: 
            return [(idx+1)%n+1, (idx+1)//n+1] #탈락이므로 결과 리턴
            #다르다면
        say_word.append(words[idx]) #탈락자 아니라면 말한 단어들 리스트에 저장
    return [0, 0]


print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]	))