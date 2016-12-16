#Ejercicio1
#Valeria Montserrat Maya Gonzalez
#Función que muestra en la pantalla las n líneas de un archivo
#Para ello se debe introducir el nombre o ruta del archivo entre comillas, y el número de líneas que se quieran leer

def leertxt(s,n):
    archivo=open(s,"r")
    for linea in range(1,(n+1)):
        lineas=archivo.readline()
        print lineas
