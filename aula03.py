# Meta caracteres: ^ $ ( )
# * 0 ou n
# + 1 ou n {1,}
# ? 0 ou 1
# {n}
# {min, max}
# {10,} 10 ou mais
# {,10} De zero a 10
# {10} Especificamente 10
# {5,10} De 5 a 10
# ()+ [a-zA-Z0-9]+

import re

texto = '''
João trouxe    flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.


Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso
pão de queijo.
Não canso de ouvir a Maria:
"Joooooooooãooooooo, o café tá prontinho aqui. Veeemm veeem veem vem"!
Jã
'''
print('Os quantificadores aplicam sua propriedade aos caracteres que estão a esquerda dele.')
print(50*'-')
print('O + aplica uma condição de existência do caractere, no caso, o O pode existir na palavra, 1 ou mais vezes')
print(re.findall(r'j[o]+ão+', texto, flags=re.I))
print(50*'-')
print('Utilizando as chaves, fica liberal dizer qual a quantidade de vezes que o caractere pode ocorrer, mais flexível')
print(re.findall(r'jo{1,}ão{1,}', texto, flags=re.I))
print(50*'-')
print('Nesse caso, a palavra deve ter especificamente 3 E e com 1 ou 2 M na sua composição')
print(re.findall(r've{3}m{1,2}', texto, flags=re.I))

texto2 = 'João ama ser amado'
print(re.findall(r'ama[od]{0,2}', texto2, flags=re.I))