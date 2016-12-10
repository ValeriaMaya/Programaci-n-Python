#Ejercicio5
#Valeria Montserrat Maya Gonzales
#Programa que recive una cantidad de segundos y los devuelve a su equivalente en días, horas, minutos y segundos

def convierte(ss)
    min=ss/60
    print min," minutos"
    hr=ss/3600
    print hr," horas"
    dd=ss/(24*3600)
    print dd," dias"
    print ss
