#Ejercicio3
#Valeria Montserrat Maya Gonzalez
#Numerar las líneas de un archivo de texto ya existente, guardarlo como un archivo independiente cuyo nombre sea especificado al inicio.

def numerar(n,m):
    v=open(n,"r")
    nvo=open(m,"w")
    for linea in v:
        l=len(v.readline())
        linea=v.readline()
        nvo.write("l) "+linea+"\n")
