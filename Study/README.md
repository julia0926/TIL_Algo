## 알고리즘 TIL🔥
- 목표 : 하루에 2문제 
- 커밋 안올라오면 바로 혼쭐 주세여,, Plz,,,🥲
---
### 에라토스테네스의 체
- 검색X, 무조건 외우기
```python
def is_prime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
```
### 딕셔너리 모듈
- `defaultdict` : 존재하지 않는 키를 조회할 경우, 에러 메세지 대신 디폴트 값을 기준으로 해당 키에 대한 딕셔너리 아이템을 생성
```python
import collections

a = collections.defaultdict(int)
a['A'] = 5
a['B'] = 4
a['C'] += 1 #디폴트 값이 0임 (int형)
print(a) #defaultdict(<class 'int'>, {'A': 5, 'B': 4, 'C': 1})
```
- `Counter` 객체 : 아이템에 대한 개수를 계산해 딕셔너리로 리턴, key(변수) - value(변수의 개수)
- most_common : 가장 빈도 수 높은 요소 추출
```python
a = [1,2,2,3,3,4,5,6]
b = collections.Counter(a)
print(b) #Counter({2: 2, 3: 2, 1: 1, 4: 1, 5: 1, 6: 1})
print(b.most_common(2)) # [(2, 2), (3, 2)] # Counter b에서 우선순위 높은 요소 2개 추출
```
### 문자열 조작
- isalnum() : 문자열이 문자(영어/한글), 숫자로 되어있으면 ? True : False
- isalpha() : 문자열이 문자(영어/한글)로 되어있으면 ? True : False
- s[::-1] : 문자열 뒤집기 
- s[::2] : 2칸씩 앞으로 이동 

### heapq란?
[대표문항 - 더맵게](https://school.programmers.co.kr/learn/courses/30/lessons/42626) / [(공식문서)](https://docs.python.org/ko/3/library/heapq.html)
- 먼저 heapq는 이진트리 기반의 최소힙을 제공함
- 우선순위 큐는 힙으로 구현된다 -> 우선순위큐는? 순서 상관없이 우선수위 높은 데이터가 먼저 나감 
- 그럼 heap은 뭐지? -> 루트를 기준으로 왼쪽 노드보다 작고 오른쪽 노드보다 크다. 힙은 완전트리이다
- 완전 이진트리란? -> 마지막 레벨을 제외하고 모든 레벨이 채워져있다
###  그래서 heapq 언제써? 
예제 문항에서 보면 새로운 값을 구할 때마다 해당 값을 넣고 그 중 제일 작은값을 구해야한다. <br>
이 때 heapq는 최소힙을 제공하므로 딱 들어맞쥬? 그리고 리스트로 하면 삽입빠르면 삭제 느림 or 삭제 빠르면 삽입 느림 이런식이라 힙큐가 더 빠르며 효율적임. <br>

<img width="690" alt="스크린샷 2022-09-17 오후 5 35 56" src="https://user-images.githubusercontent.com/37897873/190848132-f0a2fcd3-4cd5-4ea6-83fd-875a3ebf5214.png">


### count()
string.count(self, x, __start, __end) <br>
문자열 안에서 찾고 싶은 특정 문자의 개수를 찾음.
```python
str = "Hello World"
print(str.count('o')) #2
```

### replace()
String.replace(originStr, replaceStr, maxCount) <br>
문자열 안에서 특정 문자를 새로운 문자로 변경, 변경된 문자열은 새로 담아야 된다.
```python
str = "one23four"
str = str.replace("one","1") 
print(int(str))  #123four
```
### bisect_left
bisect.bisect_left(a, x, lo=0, hi=len(a), *, key=None) <br>
정렬된 a에 x를 삽입할 위치를 리턴해준다. x가 a에 이미 있으면 기존 항목의 앞 (왼쪽)의 위치를 반환
(bisect_right라면 오른쪽에)<br>
```python
from bisect import bisect_right, bisect_left

a = [1,2,3,4,4,8]
x = 4
print(bisect_left(a,x)) #3
print(bisect_right(a,x)) #5
```
### math.pow(), math.sqrt()
- math.pow(x,y) -> return float : x의 거듭 제곱 (x의 y승)을 반환 <br>
```python
math.pow(2, 4) #16
```
- math.sqrt(x) -> return float : x의 제곱근 반환(x에 루트 씌운 값) <br>
```python
math.pow(121) #11
```
### pass, continue, slicing
- pass : 단순히 실행할 코드가 없을 때 사용 <br>
- continue : 하위 문장 실행 안하고 바로 다음 반복문 동작 <br>
- slicing : 문자열이나 배열을 부분 자를 때 (ex: [:3] 앞 3개 자름, [2:] 뒤에 2개 자름, [1:3] 2~3까지)
### find()
string.find(찾을 문자, 시작 Index, 끝 Index) - 시작과 끝 인덱스 생략 가능 <br>
찾는 문자나 문자열이 존재하면 해당 위치 index 반환, 존재 안하면 -1<br>
- "adsaad" 문자열 중 d의 위치를 리턴해야 한다면 제일 앞부분인 1 리턴
### 숫자의 자릿수와 각 값 리스트에 넣기
```python
n = 123
num_n = len(123) #3이 리턴 
```
```python
for i in range(1, n):
    num_i = list(map(int, str(i))) 
print(num_i) #[1,2,3] 출력
```
### 10진수 -> 2진수
```python
print(format(10, 'b')) #1010
```
### 리스트 값 반복문 없이 바로 출력하기
- 이렇게 하면 리스트의 값을 굳이 반복문으로 벗겨낼 필요 없음
```python
res = [1,2,3,4] 
print(*res) #1 2 3 4
```
### 숫자 각 자리수를 배열로 넣기
```python
for i in range(110, 115):
    num_list = list(map(int, str(i))) 
    print(num_list)
''' 
[1, 1, 0]
[1, 1, 1]
[1, 1, 2]
[1, 1, 3]
[1, 1, 4]
'''
```
### DFS RecursionError 발생시
- 깊이의 제한을 두면 해결
```python
import sys
sys.setrecursionlimit(10000)
```
