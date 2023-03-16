# https://school.programmers.co.kr/learn/courses/4008/lessons/13246
#제일 많이 나온 횟수를 저장
#그 횟수를 가지고 알파벳 문자 찾음
#그리고 문자열에 저장해서 출력

from collections import Counter

my_str = input().strip()
counter = Counter(my_str).most_common()
max_count = counter[0][1]

result = list(filter(lambda x: x[1] == max_count, counter))
answer = ''
for i in result:
    answer += i[0]

print(''.join(sorted(answer)))