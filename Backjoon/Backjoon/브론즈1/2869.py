#브론즈1 - 달팽이는 올라가고 싶다 : https://www.acmicpc.net/problem/2869

import math

a, b, v = map(int, input().split())

#v = (a-b) * day + a
print(math.ceil((v-a)/(a-b)+1))