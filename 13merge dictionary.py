dict1=dict()
dict2=dict()

keys1=input("enter keys seperated by space for dict1:").split()
for i in keys1:
    dict1[i]=int(input("enter values to corresponding keys in dict1:"))
print("dict 1 : ",dict1)
keys2=input("enter keys seperated by spaces in dict2:").split()
for j in keys2:
    dict2[j]=int(input("enter values to corresponding keys for dict2:"))
print("dict2 :",dict2)
for i in dict1:
    if i not in dict2:
        dict2[i]=dict1[i]#here instead of using new variable and update function ,the resultant item can be directly added to dict2

    else:
        dict2[i]=dict1[i]+dict2[i]

print("after merging dict2 is modified as : ",dict2)



