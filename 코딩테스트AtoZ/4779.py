ans = ['' for _ in range(13)]
ans[0] = '-'

for i in range(1, 13):
    ans[i] = ans[i-1] + ' ' * pow(3,i-1) + ans[i-1]

while True:
    try:
        k = int(input())
        print(ans[k])
    except:
        break

