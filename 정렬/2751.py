import sys
n = int(input())
list = list(int(sys.stdin.readline().strip()) for _ in range(n))

for i in sorted(list):
    sys.stdout.write(str(i)+'\n')