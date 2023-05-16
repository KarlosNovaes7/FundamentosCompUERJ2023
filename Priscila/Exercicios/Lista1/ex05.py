a=int(input(' digite o valor do lado a do trinagulo: '))
b=int(input(' digite o valor do lado b do trinagulo: '))
c=int(input(' digite o valor do lado c do triangulo: '))
if a< b+c and b< a+c and c< a+b :
    perimetro= a+b+c
    print(" Os valores de a. b e c podem formar um trinagulo")
    print( " O perimetro do triângulo é: ",perimetro)
else:
    print(' Os valores informados não são suficientes para formar um triangulo ')

    '''
pseudocodigo
inicio
inteiro a.b,c, perimetro:
    1-leia a
    2-leia b
    3-leia c
    4- Se a< b+c E b <a+c E c<a+b Então:
        perimetro<= a+b+c
        imprimir " Os valores de a, b e c  podem formar um triangulo"
        imprimir " O perimetro do triangulo é:, perimetro"
    5-Senão:
        imprimir "os valores informados não são suficientes para formar um triangulo"
fim algoritmo
'''
