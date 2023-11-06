nome = 'Felipe Fernando'
altura = 1.72
peso = 75
imc = peso / (altura * altura)

# f-strings 

linha_1 = f'{nome} tem {altura:.2f} de altura,'
linha_2 = f'pesa {peso} seu imc é: '
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)