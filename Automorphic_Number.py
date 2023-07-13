n=int(input())
s=n*n
l=list(str(n))
l.reverse()
l1=list(str(s))
l1.reverse()
c=0
for i in range(len(l)):
    if l[i]==l1[i]:
        c+=1
if c==len(l):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")