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
