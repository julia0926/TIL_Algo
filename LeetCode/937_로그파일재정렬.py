'''
1. 앞부분 식별자
2. 숫자가 앞에
3. 문자가 동일하면 식별자 순
4. 숫자는 그대로 
'''
def solution(logs):
    alpha, digit = [], []
    for log in logs:
        if log.split()[1].isdigit():
            digit.append(log)
        else:
            alpha.append(log)
    alpha.sort(key=lambda x: (x.split()[1], x.split()[0])) #문자가 같으면 식별자 순으로 
    print(alpha+digit)

solution(["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"])