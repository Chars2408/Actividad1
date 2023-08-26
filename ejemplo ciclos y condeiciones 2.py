texto=input("ingrese un texto:\t") 
texto=texto.lower()
pi=0
la=len(texto)
pf=la
for i in range(la): 
 pi=i
 pf=la+1-3
 print (texto[pi:pf])
