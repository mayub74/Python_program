def checkprime(n):
    for i in range(2,n):
        if n%i==0:
            print(n," is not a prime number")
            break;
        elif i==n-1:
            print(n," is a prime number")
num=int(input("Enter number:"))
checkprime(num)
