#Ejercicio1
#Valeria Montserrat Maya Gonzalez

import math
def dist(lista):
  t1=(lista[0][0])*math.pi/180
  t2=(lista[1][0])*math.pi/180
  g1=(lista[0][1])*math.pi/180
  g2=(lista[1][1])*math.pi/180
  d=6371.01*math.acos(math.sin(t1)*math.sin(t2)+math.cos(t1)*math.cos(t2)*math.cos(g1-g2))
  print d,"kilometros"
