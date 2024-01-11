# Metacaracteres em Expressões Regulares no Python 3

## Introdução

As expressões regulares são uma ferramenta poderosa para buscar, manipular e validar texto com base em padrões específicos. 
Os metacaracteres desempenham um papel fundamental na definição desses padrões.

```python
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
Não canso de ouuvir a Maria:
"Joooooooooãooooooo, o café tá prontinho aqui. Veeemm"!
'''

# Exemplos de uso de metacaracteres
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
```

## Metacaracteres Comuns

### 1. `|` (OU)

O metacaractere `|` é usado para especificar alternativas. Ele permite que você escolha entre várias opções de padrões. 
Por exemplo, `João|Maria` encontrará qualquer ocorrência de "João" ou "Maria" no texto.

### 2. `.` (Ponto)

O ponto `.` representa qualquer caractere, com exceção da quebra de linha. Por exemplo, `ad....s` encontrará palavras que 
começam com "ad," têm 7 caracteres e terminam com "s".

### 3. `[]` (Conjunto de Caracteres)

Os colchetes `[]` são usados para definir um conjunto de caracteres a serem procurados. Por exemplo, `[Jj]oão` irá corresponder 
a "João" ou "joão", e `[a-z]aria` encontrará qualquer palavra que comece com qualquer letra minúscula de "a" a "z" e termine com "aria".

### 4. `[a-zA-Z0-9_]` (Intervalos e Caracteres Especiais)

Dentro de colchetes, você pode especificar intervalos de caracteres, como `[a-zA-Z0-9_]`, que corresponde a letras maiúsculas 
e minúsculas, dígitos e o caractere de sublinhado. Isso permite encontrar palavras que contenham letras ou números, independentemente 
da formatação.

### 5. `flags` (Flags)

As flags, como `re.IGNORECASE`, podem ser usadas para modificar o comportamento das expressões regulares. No exemplo, `re.IGNORECASE` 
permite encontrar palavras, como "João" e "Maria", independentemente da formatação das letras maiúsculas e minúsculas.

## Conclusão

Os metacaracteres permitem criar padrões flexíveis e poderosos para busca, manipulação e validação de texto.