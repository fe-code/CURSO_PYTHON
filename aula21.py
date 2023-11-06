# Operador Lógicos
# and (e) or (ou) not (não)
# and => Todas as condições precisam ser verdadeiras
# Se qualquer valor for considerado Falso,
# A expressão toda será avaliada naquele valor
# São considerados False
# 0 0.0 '' False
# Tambem existe o tipo None que é 
# Usado para representar um não valor!

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'

if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrou com sucesso!')
else:
    print('Voce saiu!')