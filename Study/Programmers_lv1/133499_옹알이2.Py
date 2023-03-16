'''
https://school.programmers.co.kr/learn/courses/30/lessons/133499
* 주의할점 replace로 해버리면 연속된 단어를 체크할 수 없음!
그래서, 연속되있는지 아닌지를 먼저 체크하고 변경해야함
'''

def solution(babbling):
    say_word = ["aya", "ye", "woo", "ma"]
    answer = 0

    for word in babbling:
        for text in say_word:
            if text * 2 not in word: #연속되지 않는다면
                word = word.replace(text, '*') 
        if '*'*len(word) == word:
            answer += 1
    print(answer)
    return answer
                

solution(["aya", "yee", "u", "maa"]	)
solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]	)
# solution(['yeaya'])