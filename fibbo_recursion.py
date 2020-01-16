def printFib(n):
    if(n <= 1):
        return n
    else:
        return(printFib(n-1) + printFib(n-2))
 
limit=int(input("limit:"))
print("Fibonacci sequence:")
fib=[]
for i in range(limit):
    fib.append(printFib(i))
print(fib)
