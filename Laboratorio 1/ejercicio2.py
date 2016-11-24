#Ejercicio2

interes_por_year=0.04
saldo inicial=raw_input("Cantidad a depositar")
nvo_saldo=0
for i in range(4):
    saldo=float(saldo inicial)*1.04
    nvo_saldo=nvo_saldo+saldo
    print nvo_saldo
