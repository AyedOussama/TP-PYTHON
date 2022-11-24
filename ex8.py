ch=input("donner une phrase:")
voy=['a','o','i','e','y','u']
s=0
list=ch.split(" ")
print(list)

for i in ch:
    if(i.lower() in voy):
        s+=1
        
print(f"la somme de voyelle dans la phrase {ch} est égale a {s} ")