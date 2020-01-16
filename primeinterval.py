start=int(input("enter limit :"))
prime=[]
flag=0
for i in range(start,1,-1):
    for j in range(2,i):
        if i%j==0:
            flag=1
            break    
    if flag==0:
        prime.insert(0,i)
    else:
        flag=0

print("prime numbers in given range :",prime)
        
