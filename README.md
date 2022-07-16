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
