#returns the absolute value of a number.
print("abs():")
print(abs(-7))
print(abs(2347))
print(abs(45-45))
'''returns True if all values in a python iterable have a Boolean value of True.
An empty value has a Boolean value of False.'''
print("all():")
print(all({'*','',''}))
print(all([' ',' ',' ']))
#print ascii value
print("ascii():")
print(ascii('ș'))
#print binary value
print("bin():")
print(bin(100))
# print boolean value
print("bool():")
print(bool(0.6))
print(bool(-0.6))
print(bool(0))
#print char value of ascii value
print("chr():")
print(chr(65))
print(chr(95))
print(chr(165))
#create a complex number
print("complex():")
print(complex(5))
print(complex(10.5))
#creates a dictionary
print("dir():")
d1=dict([(1,2),(3,4)])
print(d1)
'''divmod() in Python built-in functions, takes two parameters,
and returns a tuple of their quotient and remainder. In other words,
it returns the floor division and the modulus of the two numbers.'''
print("divmode():")
print(divmod(3,7))
#enumerate
print("enumerate():")
for i in enumerate(['a','b','c']):
    print(i)
#eval function
print("eval():")
x=7
print(eval('x+7*x'))
#exec() runs Python code dynamically.
print("exec():")
exec('a=2;b=3;print(a+b)')
#filter() filters out the items for which the condition is True.
print("filter():")
print(list(filter(lambda x:x%2==0,[1,2,0,False])))
# converts an int or a compatible value into a float.
print("float():")
print( float(2))
#To get details about any module, keyword, symbol, or topic, we use the help() function.
print("help():")
#print(help(math))
#Hex() Python built-in functions, converts an integer to hexadecimal.
print("hex():")
print(hex(16))
#Iter() Python built-in functions, returns a python iterator for an object.
print("iter:")
for i in iter([1,2,3]):
    print(i)
