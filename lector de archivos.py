import os
contar=os.listdir("C:/Users/madej/Downloads")
cont=0
for x in contar:
    if x.endswith(".pdf"):
        cont+=1
print("\nTotal de documentos PDF:", cont)