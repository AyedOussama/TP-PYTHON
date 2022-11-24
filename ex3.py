liste=[]
a=-1
while a<0:
    a=int(input("saisir la taille de liste : \n"))
    
    
    for i in range(a):
        b=-1
        while b<0:
               b=int(input("saisir le {} element".format(i+1)))
        liste.append(b)
        
print("le maximum valeur de liste :",max(liste))
print("le minimum valeur de liste :",min(liste))
print("la somme des elements de liste :",sum(liste))

