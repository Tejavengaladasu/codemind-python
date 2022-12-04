n=int(input())
a=[]
for i in range(1,n):
    if n%i==0:
        a.append(i)
d=sum(a)
if d>n:
    print("True")
else:
    print("False")