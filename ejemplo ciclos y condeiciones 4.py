vocales = ["A","E","I","O","U"]
texto="USAC-EFPEM"
contar=0
acciones=0
texto=texto.upper();
for i in range(len(texto)): 
 for j in range(len(vocales)):
     if(texto[i]==vocales[j]):
         contar=contar+1
         print (i, ": ", texto[i])
       
         break 
print ("Cantidad de vocales", contar)

