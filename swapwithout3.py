num1=int(input(" Enter Number 1  :"))
num2=int(input(" Enter Number 2  :"))
print(" number before swapping : Num1 = ",num1,"num2 = ",num2)
num1=num1+num2
num2=num1-num2
num1=num1-num2
print(" number after swapping : Num1 = ",num1,"num2 = ",num2)
print(" direct assinment method :")
num1,num2=num2,num1
print(" number after swapping : Num1 = ",num1,"num2 = ",num2)
