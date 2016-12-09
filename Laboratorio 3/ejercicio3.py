#Ejercicio3
#Valeria Montserrat Maya Gonzalez

print "Dame tres número enteros y los ordenaré de menor a mayor"
x1=int(input("1er Num"))
x2=int(input("2do Num"))
x3=int(input("3er Num"))
if x1>x2:
  if x2>x3:
    print x3, x2, x1
  else:
    if x1>x3:
      print x2, x3, x1
    else:
      print x2, x1, x3
else:
  if x1>x3:
    print x3, x1, x2
  else:
    if x2>x3:
      print x1, x3, x2
    else:
      print x1, x2, x3
