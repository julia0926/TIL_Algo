# PythonAlgo
✏️ 파이썬으로 푸는 알고리즘

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
