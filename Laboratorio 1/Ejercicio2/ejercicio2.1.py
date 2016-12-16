#Ejercicio 2
#Valeria Montserrat Maya Gonzalez
#Programa que lee el saldo inicial de un usuario y muestra en pantalla sus respectivos saldos al primer, segundo y tercer año, cuando el interés por año es del 4%

interes_por_year=0.04
saldo=float(input("Escriba el saldo inicial, le diré su saldo al 1er, 2do y 3er año: "))
for i in range(1,4):
    saldo=round((saldo*0.04)+saldo,2)
    print saldo
