ch="un bon étudiant est celui qui révise chaque jour son cours"
x=ch.find("bon")
ch1=ch[x:x+len("bon")]

print(ch1)
ch2 = ch[0 :x + len("bon")] +" "+ ch1*2
print(ch2)