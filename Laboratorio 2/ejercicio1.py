#Ejercicio1
#Valeria Montserrat Maya Gonzalez
#Función que recive los catetos de un triángulo rectángulo y regresa la magnitud de la hipotenusa

import math
def hip(x,y):
    hip=round(math.sqrt(math.pow(x,2)+math.pow(y,2)),2)
    print hip
