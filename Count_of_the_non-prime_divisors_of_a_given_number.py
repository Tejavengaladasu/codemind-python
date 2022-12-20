n=int(input())
l=[]

np=[]

for i in range(1,n+1):
    if n%i==0:
        l.append(i)
for j in l:
    c=0
    for k in range(1,j+1):
        if j%k==0:
            c+=1
    if c!=2:
        np.append(j)
print(len(np))        
    