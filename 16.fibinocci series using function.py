def fibo(n):
    a=0
    b=1
    print("The fibinocci series is : \n")
    for i in range(n):
        print(a)
        c=a+b
        a=b
        b=c

n=int(input("To find fibinocci series of n terms:enter the number of terms = "))
fibo(n)