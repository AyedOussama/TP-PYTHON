liste=[]
r=[]
a=int(input("saisir la taille de liste :\t "))
while a<6 or a>50 :
    a=int(input("saisir la taille de liste : \t"))
    
    
for i in range(a):
    b=-1
    while b<0 :
        b=int(input("saisir le {} element\t".format(i+1)))
    liste.append(b)
        
print(liste)
r.append(liste[0])
for i in range(1,len(liste)):
    s=r[i-1]+liste[i]
    r.append(s)
       
print(r)