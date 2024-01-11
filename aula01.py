import re

# findall- encontrar todas as ocorrências do padrão desejado no texto
# search- encontrar a primeira ocorrência e comunicar o índice do local que foi encontrado
# sub- substituir algo dentro do texto
# compile- compilar expressões regulares

print('Compilando várias vezes')
string = 'Este é um teste de expressões regulares.'
print(re.search(r'teste', string))
print(re.findall(r'teste', string))
# Realiza a troca apenas na primeira ocorrência da expressão dentro do texto,
# podendo ser == a 0 para volta ao padrão, substituindo em todas as ocorrências
print(re.sub(r'Este','ABCDE',string,count=1))

print(20*'-')

print('Compilar e reutilizar')
string2 = 'Teste número 2 sobre expressões regulares'
regexp = re.compile(r'Teste')
print(regexp.search(string2))
print(regexp.findall(string2))
print(regexp.sub('ABCD', string2))