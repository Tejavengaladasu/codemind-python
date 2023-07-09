n=int(input())
stack=[]
for i in range(n+1):
    if len(stack)>=2:
        stack.append(stack[i-1]+stack[i-2])
    else:
        stack.append(i)
if n in stack:
    print("True")
else:
    print("False")
