frase = input('Digite a frase a ser contabilizada: ')
vogais = ['AaEeIiOoUu']
espaço = [" "]
print(frase)


def Contandordevogais(X, Y):
    a = X.count(Y, [0, 1])
    e = X.count(Y, [2, 3])
    i = X.count(Y, [4, 5])
    o = X.count(Y, [6, 7])
    u = X.count(Y, [8, 9])
    totalDeVogais = (a + e + i + o + u)
    return totalDeVogais


print('A frase acima possui', len(frase), 'caracteres')
print('O total de vogais da frase foram:', Contandordevogais(frase, vogais), 'vogais')
