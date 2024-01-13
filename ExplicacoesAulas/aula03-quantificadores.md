# Quantificadores em Expressões Regulares no Python 3

## Introdução

Os quantificadores são metacaracteres em expressões regulares que especificam quantas vezes um caractere ou grupo 
de caracteres pode ocorrer em uma correspondência. Eles fornecem um meio flexível de definir a repetição de elementos em padrões de texto.

```python
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

print('Os quantificadores aplicam sua propriedade aos caracteres que estão à esquerda deles.')
print(50*'-')
```

## Quantificadores Comuns

### 1. `*` (0 ou n)

O asterisco `*` permite que um caractere ou grupo de caracteres ocorra 0 ou mais vezes. 
Por exemplo, `jo*ão*` corresponde a "João", "joão", "jooooão", etc.

### 2. `+` (1 ou n {1,})

O sinal de adição `+` requer que um caractere ou grupo de caracteres ocorra pelo menos uma vez (1 ou mais vezes). 
Por exemplo, `j[o]+ão+` corresponde a "João", 
"joão", "jooooão", mas não corresponde a "Jã".

### 3. `?` (0 ou 1)

O ponto de interrogação `?` indica que um caractere ou grupo de caracteres pode ocorrer 0 ou 1 vez. 
Por exemplo, `ve?m` corresponde a "vem" e "vm".

### 4. `{n}` (Específico)

As chaves `{n}` especificam exatamente n ocorrências do caractere ou grupo de caracteres. 
Por exemplo, `ve{3}m{1,2}` corresponde a "veeem" ou "vemm", onde "e" 
ocorre exatamente 3 vezes e "m" ocorre de 1 a 2 vezes.

### 5. `{min, max}` (Intervalo)

Chaves com um intervalo `{min, max}` especificam um número mínimo (min) e máximo (max) de ocorrências do caractere ou grupo de caracteres. 
Por exemplo, `{10,}` corresponde a 10 ou mais ocorrências, `{,10}` corresponde a até 10 ocorrências e `{5,10}` corresponde a 5 a 10 ocorrências.

## Exemplos de Uso

### Exemplo 1: Uso de `+`

O quantificador `+` é usado para encontrar palavras que contenham uma ou mais ocorrências da letra "o" seguida por "ão". Por exemplo:

```python
print(re.findall(r'j[o]+ão+', texto, flags=re.I))
```

Este exemplo corresponderá a palavras como "João", "joão", "jooooão", etc.

### Exemplo 2: Uso de `{}`

Neste exemplo, o uso de `{}` exige exatamente 3 ocorrências da letra "e" e 1 ou 2 ocorrências da letra "m". 
Portanto, ele corresponderá a palavras como "veeem" ou "vemm".

```python
print(re.findall(r've{3}m{1,2}', texto, flags=re.I))
```

## Conclusão

Os quantificadores são fundamentais para definir a repetição de caracteres ou grupos de caracteres em expressões regulares. 
Eles tornam os padrões mais flexíveis e poderosos, permitindo que você especifique a quantidade desejada de ocorrências.