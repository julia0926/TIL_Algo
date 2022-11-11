#Silver 3: 이친수 - https://www.acmicpc.net/problem/2193

n = int(input())
pinary_list = []
cnt = 0

for i in range(1, 91):
    binary = format(i, 'b')
    if len(binary) == n:
        pinary_list.append(binary)
    elif len(binary) > n:
        break

for val in pinary_list:
    if val[0] != 0:
        print(val)
        for j in range(1, len(val)):
            if val[j-1] == val[j] == '1':
                print(f'{val[j-1]} == {val[j]}  ')
                break
                #이친수 임.. 
            elif j == len(val) - 1:
                cnt += 1
            #print(j)
            

print(cnt)


