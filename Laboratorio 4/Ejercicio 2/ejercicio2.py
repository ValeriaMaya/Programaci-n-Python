#Ejercicio2
#Valeria Montserrat Maya Gonzalez
#Función que concatena archivos y los devuelve como un archivo nuevo cuyo nombre debe indicarse al inicio

def concatenar(n,m):
    nvo=open(m,"a")
    for i in n:
        c=open(i,"r")
        for linea in c:
            nvo.write(linea+"\n")
