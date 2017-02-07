#Ejercicio7
#Valeria Montserrat Maya Gonzalez

nombre=raw_input('Ingresa tu nombre' ).title()
s=map(str,nombre)
vocales=('a','e','i','o','u','A','E','I','O','U')
if nombre[0]==vocales[0] or nombre[0]==vocales[1] or nombre[0]==vocales[2] or nombre[0]==vocales[3] or nombre[0]==vocales[4]:
    new=nombre.lower()
elif nombre[0]==vocales[5] or nombre[0]==vocales[6] or nombre[0]==vocales[7] or nombre[0]==vocales[8] or nombre[0]==vocales[9]:
    new=nombre.lower()
else:
    new=nombre[1:]
    if nombre[1]==vocales[0] or nombre[1]==vocales[1] or nombre[1]==vocales[2] or nombre[1]==vocales[3] or nombre[1]==vocales[4]:
      new=new
    elif nombre[1]==vocales[5] or nombre[1]==vocales[6] or nombre[1]==vocales[7] or nombre[1]==vocales[8] or nombre[1]==vocales[9]:
      new=new
    else:
      new=new[1:]
print nombre+"!"
print nombre +",",nombre,"bo B"+new,"Bonana fanna fo F"+new,"Fee fy mo M"+new +",", nombre+"!"
