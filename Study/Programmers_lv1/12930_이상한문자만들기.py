#내풀이
def solution(s):
    answer = []
    for word in s.split(' '):
        piv = ''
        for k in range(len(word)):
            if k % 2 == 0: piv += word[k].upper()
            else: piv += word[k].lower()
        answer.append(piv)
    return ' '.join(answer)

a = solution("try hello world")


def toWeirdCase(s):
    return " ".join(map(lambda x: "".join([a.lower() if i % 2 else a.upper() for i, a in enumerate(x)]), s.split(" ")))

toWeirdCase("try hello world")