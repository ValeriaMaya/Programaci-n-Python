#Ejercicio3
#Valeria Montserrat Maya Gonzalez
#Grafica de los N puntos que se obtienen al iterar el punto Po en un triángulo

import matplotlib.pyplot as plt

print "Con el siguiente progarama haremos un juego de caos basado en un triángulo y un punto inicial 'Po'"
print "Tomaremos en primer vértice del triángulo en el origen de coordenadas. Ahora le prediremos las coordenadas de los vértices restantes:"
x2=input("Coordenada 'x' del Vértice 2:")
y2=input("Coordenada 'y' del Vértice 2:")
x3=input("Coordenada 'x' del Vértice 3:")
y3=input("Coordenada 'y' del Vértice 3:")

def vert(x2,y2,x3,y3):
    v1=[0,0]
    v2=[x2,y2]
    v3=[x3,y3]
    v=[v1,v2,v3]
    print v
def caos(Po,N,v):
    for i in range(1,N):
        p1=[((v2[0]+v3[0])/2),((v2[1]+v3[1])/2)]
        v=[v1,p1,v2]
        plt.figure('Juego del caos')
    triangulo=plt.Polygon(v,fill=None)
    plt.show()
vert(x2,y2,x3,y3)
v1=[0,0]
v2=[x2,y2]
v3=[x3,y3]
v=[v1,v2,v3]

Po=input("¿cuál vértice elige como el punto inicial? Escriba solo: v1, v2 o v3:")
N=int(input("¿cúantas veces quiere repetir el ciclo? Conteste con un número"))
if N==0:
  print "Por favor introduzca un número distinto de cero"
else:
  caos(Po,N,v)
