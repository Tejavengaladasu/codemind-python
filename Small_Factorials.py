def factorial(n):
    sum=0
    if n==1 or n==0:
        return 1
    
    return sum+n*factorial(n-1)
        
        
    
t=int(input())

for i in range(t):
    n=int(input())
    print(factorial(n))
    