## 알고리즘 TIL🔥
### 220430
- 에라토스테네스의 체 (검색X, 무조건 외우기)
```python
def is_prime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
```
