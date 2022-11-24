
mat1=[]
mat2=[]
som=[]
mi=[]
pro=[]
y=-1
while y<0:
    y=int(input("saisir la taille de liste : \n"))

for i in range(y):
      l = []
      for j in range(y):
        b=int(input("entrer un entier: "))
        l.append(b)
      mat1.append(l)     
    
print("")
print(mat1) 
print("")

for p in range(y):
    g=[]
    for d in range(y):
        b=int(input("entrer un entier: "))
        g.append(b)
    mat2.append(g)
print(end=" ")  
    
     
print (mat2)


i,j=0,0
print("le somme  de  3*a+10*b ")
for i in range(y):
    v=[]
    for j in range(y):
          s=(3*mat1[i][j])+(10*mat2[i][j])
          v.append(s)
    pro.append(v) 

print(pro)


i,j=0,0
print("la somme de matrice")
for i in range(y):
    v=[]
    for j in range(y):
          s=mat1[i][j]+mat2[i][j]
          v.append(s)
    som.append(v) 

print(som)

i,j=0,0
print("la différence entre matrice")
for i in range(y):
    v=[]
    for j in range(y):
          s=mat1[i][j]-mat2[i][j]
          v.append(s)
    mi.append(v) 

print(mi)
