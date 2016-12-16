#Ejercicio6
#Valeria Montserrat Maya Gonzalez
#Programa que devuelve el IMC de un usuario dando su peso en kilogramos y su estatura en metros

import math
print "Calcularemos su IMC"
est=float(input("Deme su estatura en metros"))
masa=int(input("Deme su peso en kilogramos"))

def IMC(m,e):
  imc=round(m/(math.pow(e,2)),2)
  print "Su Indice de masa corporal es ", imc,", dictamen..."
  if imc<16:
      print "Delgadez severa"
  else:
      if imc<=16.99:
          print "Delgadez moderada"
      else:
          if imc<=18.49:
              print "Delgadez Leve"
          else:
              if imc<=24.99:
                  print "Normal"
              else:
                  if imc<=25:
                      print "Sobrepeso"
                  else:
                      if imc<=30:
                          print "Obesidad"
                      else:
                        print "Obesidad mórbida"

IMC(masa,est)
