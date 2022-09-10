nota1=(float(input('Qual é a sua nota da P1? ')))
nota2=(float(input('Qual é a sua nota da P2? ')))
media=((nota1+nota2)/2)
if media >= 7.0:
    print("Aluno Aprovado!")
elif  media >= 4.0 and media< 7.0:
    print("Aluno de PF!")
else:
    print('Aluno reprovado!')

print(type(media))

print('Esté é o meu primeiro programa em Python utilizando a IDE da Jetbrains, o PyCharm')