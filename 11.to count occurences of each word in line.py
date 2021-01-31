sentence=input("enter a sentence =")
lower=sentence.lower()
word=lower.split()#converted to list by default
print("converted to list of words in the form",word)
d=dict()
for i in word:
    if i in d:
        d[i]=d[i]+1
    else:
        d[i]=1
print(d)
for key in list(d.keys()):
    print(key,":",d[key])

