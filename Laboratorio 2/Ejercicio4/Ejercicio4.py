#Ejercicio4
#Valeria Montserrat Maya Gonzalez
#Función que recibe como argumento de entrada un entero n y devuleve la lista que contiene las coordenadas de un polígono regular de n lados

import math as m

def figura(n):
  Cc=[(1,0)]
  a_int=360/n
  for i in range(1,n):
    a_intf = a_int * i
    print a_intf
    a_rad = m.radians(a_intf)
    x = round(m.cos(a_rad),2)
    y = round(m.sin(a_rad),2)
    v = (x,y)
    Cc.append(v)
  print Cc
