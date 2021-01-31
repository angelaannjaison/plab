string=input("enter a string=" )
first_char=string[0]#acces first char
l=string[1:]#to access (string-first char)
for char in l:
    m=l.replace(first_char,'$')
print(first_char+m)#concatenate