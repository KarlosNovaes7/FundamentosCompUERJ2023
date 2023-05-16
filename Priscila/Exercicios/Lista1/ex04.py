print(' Bem vindo a calculadora em Python \n')
print(' digite 1 para: adição | digite 2 para: Subtração | digite 3 para : multiplicação | digite 4 para : divisão \n')
n1=float(input(' digite o 1° número: \n'))
n2=float(input('digite o 2° número: \n'))
opcao=int(input(' agora digite as opções ( de 1 a 5)'))

if opcao == 1:
    print(f'Você escolheu a opção Adicão !\n')
    print(f' O resultado é : {n1+n2}')
elif opcao == 2:
    print(f'Você escolheu a opção Subtração !\n')
    print(f' O resultado é : {n1-n2}')
elif opcao == 3:
    print(f'Você escolheu a opção Multplicação !\n')
    print(f' O resultado é : {n1*n2}')
elif opcao == 4:
    print(f'Você escolheu a opção Divisão !\n')
    print(f' O resultado é : {n1/n2}\n')
    print(f'e o resto da divisão é: {n1%n2}')
else: 
    print(' voce saiu da Calculadora !')
    '''
pseudocódigo
inicio algoritmo
    1-float n1, n2, opcao;
    2-imprimir " Bem vindo a calculadora!"
    3-imprimir "  digite 1 para: adição | digite 2 para: Subtração | digite 3 para : multiplicação | digite 4 para : divisão'
    4-leia n1
    5- leia n2
    6- leia opcão
    7- Se opcao igual a 1 Então:
        imprimir "n1+n2"
        imprimir " Operação de Adicção"
    8- Se opcao igual a 2 Então:
        imprimir "n1-n2"
        imprimir " Operação de Subtração"
    9- Se opcao igual a 3 Então:
        imprimir "n1*n2"
        imprimir " Operação de Multiplicação"
    10- Se opcao igual a 4 Então:
        imprimir "n1/n2"
        imprimir " Operação de Divisão"
        imprimir" resto da divisão: n1%n2"
    11- Senao
        imprimir "Voce Saiu da Calculadora !"
fim algoritmo
'''
    
