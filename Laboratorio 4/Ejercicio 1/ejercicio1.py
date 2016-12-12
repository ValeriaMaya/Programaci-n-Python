def leertxt('name',n):
    archi=open('name','r'):
    it=(linea for i, linea in enumerate(archi) if i>=n)
    for linea in it:
        print linea
