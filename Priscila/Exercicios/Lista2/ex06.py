num=int(input('digite o numero a ser fatorado: '))
fatorial=1
cont=2

while cont<=num:
    fatorial=fatorial*cont
    cont=cont+1
    print(fatorial)
print(f'o fatorial de {num} é {fatorial}')
    
