vet=[]
contadorpar=0
for i in range (0,10):
    num=int(input('Digite o número: '))
    vet.append(num)
print('Os números foram:')
print(vet)
for i in range(0,10):
    if vet[i]%2==0:
        contadorpar=contadorpar+1
print('Quantidade de números pares:',contadorpar)
