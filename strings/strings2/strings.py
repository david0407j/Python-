frase = 'ola, bem-vindo, a este treinamento!'

print(frase.split())
print(frase.split(','))
print(frase.split(','))

nomes = 'davidson, cleite, carol, jane, bruna, barbara'

print(nomes.split())
print(nomes.split(','))

hashtags = 'music #guitar #gamer #coder #python'
print(hashtags.split())
print(hashtags.split('#'))
print(hashtags.split('#', 3))

# como concatenar(combinar) strings

hashtags_separados_por_espaco = hashtags.split(' ')
print(hashtags_separados_por_espaco)
print(','.join(hashtags_separados_por_espaco))
print(','.join(hashtags_separados_por_espaco))
print(','.join(hashtags_separados_por_espaco))