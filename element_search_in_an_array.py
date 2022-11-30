n=int(input())
l=list(map(int,input().split()))
m=int(input())
cp=0
for i in l:
    if m==i:
        cp+=1
if cp>0:
    print("True")
else:
    print("False")