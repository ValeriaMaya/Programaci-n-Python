#Ejercicio2
#Valeria Montserrat Maya Gonzalez
#Función que concatena archivos y los devuelve como un archivo nuevo cuyo nombre debe indicarse al inicio
#Para ello debe introducirse una lista [], cuyos elementos sean las rutas o nombres de archivos entre comillas y, el nombre, también entre comillas, qu se quiere dar al nuevo archivo al concatenar los anteriores.
def concatenar(n,m):
    nvo=open(m,"a")
    for i in n:
        c=open(i,"r")
        for linea in c:
            nvo.write(linea+"\n")
