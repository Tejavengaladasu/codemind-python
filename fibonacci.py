n=int(input())
stack=[]
for i in range(n):
    if len(stack)>=2:
        stack.append(stack[i-1]+stack[i-2])
    else:
        stack.append(i)
print(*stack)
        