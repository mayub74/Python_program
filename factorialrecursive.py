def printfact(n):
    if(n <= 1):
        return n
    else:
        return(n*printfact(n-1))
 
num=int(input("Enter number:"))
print("Factorial :",printfact(num))
