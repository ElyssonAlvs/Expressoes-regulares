# Expressões Regulares em Python 3: Greedy vs. Non-Greedy

## Introdução

O conceito de expressões regulares em Python 3, focando especialmente nas diferenças entre a abordagem 
"greedy" (gananciosa) e "non-greedy" (preguiçosa ou lazy).

## Meta Caracteres Utilizados

Antes de explorar as nuances de "greedy" e "non-greedy", é importante compreender alguns meta caracteres fundamentais:

- `^`: Representa o início da linha.
- `$`: Representa o final da linha.
- `()`: Utilizado para agrupar expressões.
- `*`: Corresponde a 0 ou mais ocorrências.
- `+`: Corresponde a 1 ou mais ocorrências.
- `?`: Indica 0 ou 1 ocorrência.

## Exemplo de Código

O código de exemplo abaixo utiliza expressões regulares para extrair padrões específicos de um texto:

```python
import re

texto = '''
<p>Frase 1</p> <p>Eita</p> <p>Qualquer frase</p> <div>1</div> 
'''

# Expressão Greedy
print(re.findall(r'<[dpiv]{1,3}>.+<\/[dpiv]{1,3}>', texto))

# Expressão Non-Greedy
print(re.findall(r'<[dpiv]{1,3}>.+?<\/[dpiv]{1,3}>', texto))
```

## Greedy vs. Non-Greedy

### Expressão Greedy

Na primeira chamada `re.findall`, a expressão regular `r'<[dpiv]{1,3}>.+<\/[dpiv]{1,3}>'` utiliza o quantificador `+` 
de maneira gananciosa. Isso significa que ele tentará corresponder ao máximo possível de caracteres entre as tags `< >`.

### Expressão Non-Greedy

Já na segunda chamada `re.findall`, a expressão regular `r'<[dpiv]{1,3}>.+?<\/[dpiv]{1,3}>'` incorpora o `?` ao quantificador `+`, 
tornando-o não ganancioso. Dessa forma, ele tentará corresponder ao mínimo possível de caracteres entre as tags `< >`.

## Conclusão

Ao compreender e utilizar a distinção entre "greedy" e "non-greedy", é possível refinar as buscas em padrões específicos dentro de 
textos, proporcionando maior flexibilidade e precisão no processamento de dados com expressões regulares.