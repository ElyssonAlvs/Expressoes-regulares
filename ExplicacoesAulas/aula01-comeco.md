# Expressões Regulares em Python 3

## Introdução

As expressões regulares, também conhecidas como **regex** ou **regexp**, são uma poderosa ferramenta utilizada para buscar, 
manipular e validar texto com base em padrões específicos. No Python, o módulo `re` fornece suporte para trabalhar com expressões regulares,
incluindo o uso do módulo `re` e as principais funções: `findall`, `search`, `sub` e `compile`. Utilizando o seguinte código, é 
possível entender os conceitos.

```python
import re

# findall - encontrar todas as ocorrências do padrão desejado no texto
# search - encontrar a primeira ocorrência e comunicar o índice do local que foi encontrado
# sub - substituir algo dentro do texto
# compile - compilar expressões regulares

print('Compilando várias vezes')
string = 'Este é um teste de expressões regulares.'
print(re.search(r'teste', string))
print(re.findall(r'teste', string))
# Realiza a troca apenas na primeira ocorrência da expressão dentro do texto,
# podendo ser == a 0 para voltar ao padrão, substituindo em todas as ocorrências
print(re.sub(r'Este','ABCDE',string,count=1))

print(20*'-')

print('Compilar e reutilizar')
string2 = 'Teste número 2 sobre expressões regulares'
regexp = re.compile(r'Teste')
print(regexp.search(string2))
print(regexp.findall(string2))
print(regexp.sub('ABCD', string2))
```

## Funções Principais

### 1. `re.search(pattern, string)`

A função `search` é utilizada para encontrar a primeira ocorrência de um padrão (`pattern`) dentro de uma string (`string`). 
Ela retorna um objeto match se encontrar o padrão ou `None` se não encontrar. No exemplo:

```python
print(re.search(r'teste', string))
```

A função `search` procura o padrão "teste" na string `string` e retorna um objeto match se encontrado. 
O resultado inclui informações sobre onde o padrão foi encontrado na string.

### 2. `re.findall(pattern, string)`

A função `findall` é usada para encontrar todas as ocorrências de um padrão (`pattern`) dentro de uma string (`string`). Ela retorna uma lista de todas as correspondências encontradas. No exemplo:

```python
print(re.findall(r'teste', string))
```

A função `findall` procura o padrão "teste" na string `string` e retorna uma lista com todas as ocorrências encontradas.

### 3. `re.sub(pattern, replacement, string, count=0)`

A função `sub` permite substituir todas as ocorrências de um padrão (`pattern`) por uma string de substituição (`replacement`) 
em uma string de origem (`string`). O argumento opcional `count` permite especificar o número máximo de substituições a serem feitas 
(padrão é 0, que significa substituir todas as ocorrências). No exemplo:

```python
print(re.sub(r'Este', 'ABCDE', string, count=1))
```

A função `sub` substitui a primeira ocorrência de "Este" na string `string` por "ABCDE" e retorna a string resultante.

### 4. `re.compile(pattern)`

A função `compile` é usada para compilar uma expressão regular em um objeto regex que pode ser reutilizado. Isso é útil 
quando você deseja executar a mesma expressão regular várias vezes, economizando tempo de compilação. No exemplo:

```python
regexp = re.compile(r'Teste')
print(regexp.search(string2))
print(regexp.findall(string2))
print(regexp.sub('ABCD', string2))
```

Aqui, a expressão regular "Teste" é compilada em um objeto `regexp`, que é então usado para realizar a busca, encontrar todas as 
correspondências e fazer substituições na string `string2`.

## Conclusão

As expressões regulares em Python 3, juntamente com o módulo `re`, são uma ferramenta poderosa para trabalhar com padrões de texto. 
As funções `search`, `findall`, `sub` e a capacidade de compilar expressões regulares facilitam a busca, manipulação e substituição 
de texto de acordo com padrões específicos. 