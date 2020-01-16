n1,n2=0,1
limit=int(input("enter limit :"))
print("fibbonacci series is : " )
print(n1)
print(n2)
for i in range(0,limit):
    n3=n1+n2
    print(n3)
    n1=n2
    n2=n3
    
    
