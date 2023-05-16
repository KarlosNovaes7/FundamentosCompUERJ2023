n1=int(input('Digite o primeiro numero: '))
troca=0
print(f'o número digitado foi {n1}\n')
n2=int(input('Agora digite o segundo número: '))
print(f'o segundo número digitado foi {n2} \n')
print('realizando transferência... \n')
troca=n1
n1=n2
n2=troca
print('... \n')
print(' Troca realizada ! \n')
print(f' Agora o primeiro número é {n1} e o segundo é {n2}')

'''
pseudocódigo
inicio algoritmo
inteiro n1,n2,troca:
1-leia n1
2-troca <- 0
3-imprima " O número digitado foi: ",n1
4-leia n2
5-imprima " O  segundo número digitado foi: ",n2
6-imprima " realizando transferência... "
7- troca <-n1
8-n1 <- n2
9- n2<- troca
10-imprima " Troca realizada  "
11-imprima " Agora o primeiro número é: ",n1,"e o segundo é :",n2'
fim algoritmo
'''
