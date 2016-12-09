#Ejercicio6
#Valeria Montserrat Maya Gonzalez

print "Diga una edad, y le diré el equivalente en años perro"
x=float(input())
if x<0:
  print "Error, no hay edades negativas"
else:
  if x<=2:
    edad=x*10.5
    print edad
  else:
    edad=((x-2)*4)+21.0
    print edad
