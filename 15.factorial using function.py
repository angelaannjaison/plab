def fact(n):
    f=1
    if n==0:print("The factorial of ",n,"is 1")
    elif(n<0):print("factorial does not exit for negative numbers")
    else:
        for i in range(1,n+1):
            f=f*i
        print("The factorial of ",n,"is",f)


n=int(input("To find factorial:enter a number = "))
fact(n)