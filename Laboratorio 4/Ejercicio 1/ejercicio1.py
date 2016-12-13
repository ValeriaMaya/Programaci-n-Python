def leertxt(s,n):
    archivo=open(s,"r")
    for linea in range(1,(n+1)):
        lineas=archivo.readline()
        print lineas
