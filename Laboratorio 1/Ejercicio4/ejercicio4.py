#Ejercicio 4
#Valeria Montserrat Maya Gonzalez
#Covierte el tiempo de un viaje que puede ser dado en días, horas, minutos y/o segundos, y devuelve su equivalente en segundos

def calcularaseg[dd,hh,mm,ss]:
    a=dd*24*60*60
    b=hh*60*60
    c=mm*60
    seg=a+b+c+ss
    print "Tiempo en segundos",seg
