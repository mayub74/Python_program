def area(shape,l):
    if shape=="square":
        return l**2
    elif shape=="circle":
        return 3.14*l**2
    else:
        return 0

sh=input("enter shape:")
le=int(input("enter side or radius:"))
ar=area(sh,le)
print("area :",ar)
