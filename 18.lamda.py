area_square=lambda s:s*s
area_rectangle=lambda l,b:l*b
area_triangle=lambda s,a,b,c:(s*(s-a)*(s-b)*(s-c))**0.5

print("----------AREA OF SQUARE----------")
s=int(input("enter length of the side = "))
print(area_square(s))

print("\n--------AREA OF RECTANGLE---------")
l=int(input("enter length ="))
b=int(input("enter breadth ="))
print(area_rectangle(l,b))

print("\n---------AREA OF TRIANGLE---------")
a=int(input("enter side A ="))
b=int(input("enter side B ="))
c=int(input("enter side C ="))
s=(a+b+c)/2
print(area_triangle(a,b,c,s))