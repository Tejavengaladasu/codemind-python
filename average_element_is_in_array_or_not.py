n=int(input())
l=list(map(int,input().split()))
a=sum(l)//n
cp=0
for i in l:
    if a==i:
        cp+=1
if cp>0:
    print("True")
else:
    print("False")