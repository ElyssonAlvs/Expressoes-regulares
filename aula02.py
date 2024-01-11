# Meta caracteres: . ^ $ * + ? { } [ ] \ | ( )
# | OU
# . Qualquer caractere (com exceção da quebra de linha)
# [] conjunto de caracteres

import re

texto = '''
João trouxe    flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.


Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso
pão de queijo.
Não canso de ouvir a Maria:
"Joooooooooãooooooo, o café tá prontinho aqui. Veeemm"!
'''
print ('Vai selecionar João ou Maria, ou qualquer caractere que comece com ad,\ntenha 7 letras e termine com s')
print(re.findall(r'João|Maria|ad....s', texto))
print(50*'-')
print('Encontrar as duas palavras, mudando apenas a primeira letra')
print(re.findall(r'João|joão|Maria', texto))
print(50*'-')
print('''Vai encontrar as palavras utilizando [] e
delimitando que pode começar com J ou j
e nos caracteres seguintes, oão, fazendo uma
busca mais abrangente no texto ''')
print(re.findall(r'[Jj]oão|[Mm]aria', texto))
print(50*'-')
print('''Vai encontrar qualquer palavra que tenha
dentro do range de a-z e termine com aria''')
print(re.findall(r'[a-z]aria', texto))
print(50*'-')
print('''Encontra qualquer palavra com iniciais maiúsculo
ou minúsculo ou também arranjos numéricos''')
print(re.findall(r'[a-zA-Z0-9_.]aria|[a-zA-Z0-9]oão', texto))
print(50*'-')
print('''Flags mudam o comportamento que as expressões funcionam,
no caso, ele vai encontrar as palavras em qualquer formatação''')
print(re.findall(r'jOãO|mAriA', texto, flags=re.IGNORECASE))