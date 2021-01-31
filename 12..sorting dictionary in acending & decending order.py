#here keys are arranged in acending & decending order
d=dict()
keys=input("enter keys in dictionary: ").split()
for i in keys:
    d[i]=input("enter value corresponding to the key, "+i+" :")
print(d)
print("keys in dictionary sorted in ascending order: ")
for i in sorted(keys):
    print(i+" - "+d[i])
print("keys in dictionary sorted in decending order: ")
for i in sorted(keys,reverse=True):
    print(i+" - "+d[i])