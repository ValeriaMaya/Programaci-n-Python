#Ejercicio 3
#Valeria Montserrat Maya Gonzalez
#Programa que recive un radio, y regresa el area y volumen de un círculo con ese radio

import math
r=int(input("Deme un radio"))
area=round(math.pi*r*r,2)
print "area circulo en u2", area
volumen=round(4/3*math.pi*r*r*r,2)
print "volumen esfera en u3", volumen
