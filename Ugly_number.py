n=int(input())
l=[]
c=0

for i in range(1,n+1):
    if n%i==0:
        l.append(i)
for i in l:
    if i==2 or i==3 or i==5:
        c+=1
if n==1:
    print("Ugly Number")
elif c==0:
    print("Not Ugly Number")
else:
    print("Ugly Number")
