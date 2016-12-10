#Ejercicio2
#Valeria Montserrat Maya Gonzalez
#Función que resive una distancia en kilómetros y devulve el valor de la tarifa del taxi

def tarifa(d):
    tf=8.74
    tarifa=(d/0.25)*1.84
    saldo=tarifa+tf
    print saldo,"pesos"
