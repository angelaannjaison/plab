class rectangle():
    def __init__(self,l,b):
        self.__length=l
        self.__breadth=b
        self.area=self.__length*self.__breadth
    def display(self):
        print("Area =",self.area)
    def __lt__(self,a2):
        if self.area<a2.area:
            print("Rectangle 2 has greater area than rectangle 1")
        else:
            print("Rectangle 1 has greater area than rectangle 2")


print("RECTANGLE 1")
l1=int(input("Enter length of rec 1 ="))
b1=int(input("Enter breadth of rec 1 ="))
r1=rectangle(l1,b1)
r1.display()
print("RECTANGLE 2")
l2=int(input("Enter length of rec 2 ="))
b2=int(input("Enter breadth of rec 2 ="))
r2=rectangle(l2,b2)
r2.display()
r1<r2