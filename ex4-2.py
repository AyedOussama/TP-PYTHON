

'''


'''
l=[]

x=float(input("saisir un entier décimale"))
a=str(x)
x=a.index(".")
a=a[x+1:]
   
for i in range(len(a)):
    l.append(int(a[i]))
print(l)

          