A=int(5000000)
B=int(7000000)
tx_A=float(0.03)
tx_B=float(0.02)
ano=0
while A < B:
    ano=ano+1
    A=A+(A*tx_A)
    B=B+(B*tx_B)
print(f' Serão necenssários {ano} anos para que a cidade A seja maior que B:')
print(A)
print(B)
    
