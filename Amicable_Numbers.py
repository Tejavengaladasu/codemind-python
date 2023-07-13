m=int(input())
n=int(input())
l1=[]
l2=[]
for i in range(1,m+1):
    if m%i==0:
        l1.append(i)
for i in range(1,n+1):
    if n%i==0:
        l2.append(i)
if sum(l1)==sum(l2):
    print("Amicable")
else:
    print("Not Amicable")