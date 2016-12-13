#Ejercicio3
#Valeria Montserrat Maya Gonzalez
#Numerar las líneas de un archivo de texto ya existente, guardarlo como un archivo independiente cuyo nombre sea especificado al inicio.

def numerar(n,m):
    v=open(n,"r")
    nvo=open(m,"w")
    nLines=0
    for currLine in v:
        nLines=nLines+1
        for linea in v:
            nvo.write(nLines+linea+"\n")
