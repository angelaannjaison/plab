print("To find the largest among three numbers")
A = int(input("Enter first number = "))
B = int(input("Enter second number = "))
C = int(input("Enter third number = "))
if A>B and A>C:
    print(A," is greatest")
elif B>C:
    print(B," is greatest")
else:
    print(C,"is greatest")

