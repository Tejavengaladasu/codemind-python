import math
def prime(i):
    if i==1:
        return False
    sq=int(math.sqrt(i))
    for j in range(2,sq+1):
        if i%j==0:
            return False
    return True
m=int(input())
n=int(input())
c=0
for i in range(m,n+1):
    if prime(i):
        c+=1
print(c)        