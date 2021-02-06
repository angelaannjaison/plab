num_1=int(input(" enter first number ="))
num_2=int(input("enter second number ="))

if num_1>num_2:small_val=num_2
else:small_val=num_1

for i in range(1,small_val+1):
    if ((num_1 % i==0 )and (num_2 % i==0)):
        gcd=i
print("GCD of %d and %d is %d" %(num_1,num_2,gcd))