deslocamento=float(input(' Digite o tamanho do trajeto entre dois pontos em Quilometros: \n'))
velocidade=float(input(' Agora digite a sua velocidade por hora no trajeto : \n'))
tempo=(deslocamento/velocidade)
print(f' O tempo descrito no trajeto selecionado foi de: {tempo} horas')

''' pseudocódigo
inicio algoritmo
 float deslocamento, velocidade, tempo:
 leia deslocamento
 leia velocidade
 tempo <= deslocamento/velocidade
 imprima velocidade
fim
'''
