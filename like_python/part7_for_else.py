arr = [int(input()) for _ in range(5)]
result = 1
for value in arr:
    result *= value
    if int(result ** 0.5) ** 2 == result:
        print("found")
        break
else:
    print("not found")
