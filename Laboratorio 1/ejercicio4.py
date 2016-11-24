#Ejercicio 4

def calcularaseg[dd,hh,mm,ss]:
    a=dd*24*60*60
    b=hh*60*60
    c=mm*60
    seg=a+b+c+ss
    print "Tiempo en segundos",seg
