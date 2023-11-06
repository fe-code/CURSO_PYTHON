# Operador Lógicos
# and (e) or (ou) not (não)
# or => qualquer condição precisam ser verdadeira
# Se qualquer valor for considerado verdadeiro,
# A expressão toda será avaliada naquele valor
# São considerados False
# 0 0.0 '' False
# Tambem existe o tipo None que é 
# Usado para representar um não valor!

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'

if (entrada == 'E' or entrada == 'e' ) and senha_digitada == senha_permitida:
    print('Entrou com sucesso!')
else:
    print('Voce saiu!')


# Avaliação de curto circuito

