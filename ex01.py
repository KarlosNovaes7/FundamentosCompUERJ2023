temp_Celsius = []
temp_Fareinheit= []
soma_Celsius = 0
soma_Fareinheit = 0
cont_Celsius = 0
cont_Fareinheit = 0
cont_acimadamedia = 0
for i in range(0, 5):
    c = float(input('Digite as temperaturas em Celsius: '))
    soma_Celsius = soma_Celsius + c
    cont_Celsius = cont_Celsius + 1
    temp_Celsius.append(c)
    f = float((1.8 * c + 32))
    soma_Fareinheit = soma_Fareinheit + f
    cont_Fareinheit = cont_Fareinheit + 1
    temp_Fareinheit.append(f)
print('Temperatura em Celsius:', temp_Celsius)
print('Temperatura em Fareinheit:  ',temp_Fareinheit)
media_Celsius = soma_Celsius / float(cont_Celsius)

media_Fareinheit = soma_Fareinheit / float(cont_Fareinheit)
for i in range(0, 5):
    if temp_Fareinheit[i] > media_Fareinheit:
        cont_acimadamedia = cont_acimadamedia + 1
    print('Média em Celsius: %2f '%media_Celsius)
    print('Média em Fareinheit: %2f ' %media_Fareinheit)
    print('Temperaturas acima da média:  ',cont_acimadamedia)
