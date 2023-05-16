num=int(input(' digite o numero'))
if num <= 1:
    print( ' o numero não é primo')
else:
    primo = True
    
    for i in range(2,num):
        if num % i == 0:
            primo = False
            break
    if primo :
        print('é num primo')
    else:
        print(' nao é num primo')
