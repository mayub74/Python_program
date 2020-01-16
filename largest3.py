num=[]
for i in range(0,3):
   # print(i)
    a=int(input("enter number"))
    num.insert(i,a)
print("Your numbers are :")
#for i in range(0,3):
print(num)
print("Largest Number is :")
if num[0]>num[1] & num[0]>num[2]:
    print(num[0])
elif num[1]>num[0] & num[1]>num[2]:
    print(num[1])
else:
    print(num[2])
    
