def solution(num):
    count = 0
    if num == 1:
        return 0
    def calculate(num):
        nonlocal count
        if num % 2 == 0:
            num //= 2
        else:
            num = (num * 3) + 1
        count += 1
        return num

    while True:
        num = calculate(num)

        if num == 1:
            return count
        elif count > 500:
            return -1

print(solution(6))