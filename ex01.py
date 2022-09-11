import math
temp_Celsiuslist = []
temp_Fareinheitlist= []
float=[]
soma_Celsius = 0
soma_Fareinheit = 0
cont_Celsius = 0
cont_Fareinheit = 0
cont_acimadamedia = 0
for i in range(0, 5):
    c = float[input('Digite as temperaturas em Celsius: ')]
    soma_Celsius = soma_Celsius + c
    cont_Celsius = cont_Celsius + 1
    temp_Celsiuslist.append(c)
    f = float((1.8 * c + 32))
    soma_Fareinheit = soma_Fareinheit + f
    cont_Fareinheit = cont_Fareinheit + 1
    temp_Fareinheitlist.append(f)
    for element in temp_Fareinheitlist:
        float.append(float(element))

print('Temperatura em Celsius:', temp_Celsiuslist)
print('Temperatura em Fareinheit: {0:4.2f} '.format(float))
media_Celsius = soma_Celsius / float(cont_Celsius)

media_Fareinheit = soma_Fareinheit / float(cont_Fareinheit)
for i in range(0, 5):
    if temp_Fareinheitlist[i] > media_Fareinheit:
        cont_acimadamedia = cont_acimadamedia + 1
print('Média em Celsius: %5.2f '%media_Celsius)
print('Média em Fareinheit: %5.2f ' %media_Fareinheit)
print('Temperaturas acima da média:  ',cont_acimadamedia)
