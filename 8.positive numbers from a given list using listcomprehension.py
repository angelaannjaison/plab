list_integer=[]
list_integer=[int(i) for i in (input("enter integers to be included in a list = ")).split()]
list_positive=[]
list_positive=[i for i in list_integer if i>0]
print("list of positive integers are ",list_positive)