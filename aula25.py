"""
Interpolação Básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)

"""

nome = 'Felipe'
preco = 1000.95897643
variavel = '%s, o preço é R$%.2f' % (nome, preco)


print(variavel)

print('O Hexadecimal de %d é %08X' % (5050, 5050))