n = 100

def isPrime(a):
    if(a<2):
        return False
    for i in range(2,a): #2~a까지
        if(a%i==0): #나눠지면 
            return False
        return True

for i in range(n):
    if(isPrime(i)):
        print(i)