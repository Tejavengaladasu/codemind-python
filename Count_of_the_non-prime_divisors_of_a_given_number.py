def isprime(n):
    ca=0
    for i in range(1,n+1):
        if n%i==0:
            ca+=1
    if ca==2:
        return True
    else:
        return False

n=int(input())
l=[]
c=0
for i in range(1,n+1):
    if n%i==0:
        l.append(i)
for i in l:
    if isprime(i)==False:
        c+=1
print(c)
        