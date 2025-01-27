
def solution(letters):
    upper = {}
    lower = {}
    for i, char in enumerate(letters):
        if char.islower():
            lower[char] = i
        elif char.isupper():
            lower_char = char.lower()
            if lower_char not in upper:
                upper[lower_char] = i
        
        # elif char.isupper():
        #     lower_char = char.lower()
        #     if lower_char not in upper:
        #         upper[lower_char] = i
    count = 0
    for char in lower:
        if char in upper and lower[char] < upper[char]:
            count += 1
    return count

# 테스트
print(solution("aaAbcCABBc"))  # 예상 결과: 2
print(solution("xyzXYZabcABC"))  # 예상 결과: 6
print(solution("ABCabcAefG"))  # 예상 결과: 0