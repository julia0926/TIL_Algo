#https://leetcode.com/problems/remove-duplicate-letters/
#참고 영상 : https://www.youtube.com/watch?v=2ayws5Y-WM4

#사전식이라는게 acbd > adbc 즉, 사전으로 봤을 때 앞문자일수록 더 빨리 와야하는 순서임 
from collections import Counter
def removeDuplicateLetters(s) -> str:
    d = {char: idx for idx, char in enumerate(s)}
    
    res = []

    for idx, char in enumerate(s):
        if char not in res:
            #비교할 res가 있고, s의 중복값의 마지막 숫자가 아니면서, 사전순보다 작다면 -> 빼야함 
            while res and idx < d[res[-1]] and char < res[-1]:#정답이라면 char가 더 먼저 와야한다.
                '''
                ['c'] 1 7 b c
                ['b'] 2 6 a b
                '''
                print(res, idx, d[res[-1]],char, res[-1])
                res.pop()
            res.append(char)

    return "".join(res)
        

print(removeDuplicateLetters("cbacdcbc"))