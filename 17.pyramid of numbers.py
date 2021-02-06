def pyramid(n):
    for i in range(1,n+1):#num of rows
        for j in range(1,i+1):#num of columns
            print(i*j,end=" ")
        print("\n")#line space
n=int(input("To construct number pyramid:Enter number of rows and columns: "))
pyramid(n)