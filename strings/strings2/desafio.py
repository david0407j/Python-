frase1 = 'desafio manipulação de strings'
frase2 = 'davidson, carol, cleide, camilla '

### solução ## 
palavras1 = frase1.split()
palavras2 = frase2.split(',')
print(','.join(palavras1))
print(','.join(palavras2))