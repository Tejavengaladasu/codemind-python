def is_prime(m):
    cp=0
    r=0
    while m:
        d=m%10
        m=m//10
        r=r*10+d
    for j in range(1,r+1):
        if r%j==0:
            cp+=1
    if cp==2:
        print("circular prime")
    else:
        print("prime but not a circular prime")
        
    
m=int(input())
c=0
for i in range(1,m+1):
    if m%i==0:
        c+=1
if c==2:
    is_prime(m)
else:
    print("not prime")
