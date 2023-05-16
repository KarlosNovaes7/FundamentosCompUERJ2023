contador=0
i=85
j=907
soma=0
while i<j+1:
    if i %2==0:
        print(i)
        contador=contador+1
        soma=soma+i
    i=i+1
print(f' a soma de todos os valores é: {soma}')
