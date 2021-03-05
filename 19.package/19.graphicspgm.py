from graphics import rectangle,circle
from graphics.dgraphics import cuboid,sphere

print("----------CIRCLE-------------")
r=int(input("Enter radius ="))
print("Area of the circle is ",circle.circle_area(r))
print("Perimeter of the circle is ",circle.circle_perimeter(r))

print("-----------RECTANGLE-----------")
l=int(input("Enter length ="))
b=int(input("Enter breadth ="))
print("Area of the rectangle is ",rectangle.rectangle_area(l,b))
print("Area of the rectangle is ",rectangle.rectangle_perimeter(l,b))

print("-------------CUBOID----------------")
l=int(input("Enter length ="))
b=int(input("Enter breadth ="))
h=int(input("Enter height ="))
print("Area of the cuboid is ",cuboid.cuboid_area(l,b,h))
print("Perimeter of the cuboid is ",cuboid.cuboid_perimeter(l,b,h))

print("--------------SPHERE------------------")
r=int(input("Enter radius ="))
print("Area of the sphere =",sphere.sphere_area(r))
print("Perimeter of the sphere =",sphere.sphere_perimeter(r))
