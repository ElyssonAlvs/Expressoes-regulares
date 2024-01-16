# Resumo Didático: Validando CPF com Negative Lookahead em Expressões Regulares no Python 3

As expressões regulares são padrões utilizados para buscar e manipular texto. No contexto de validação de CPF 
(Cadastro de Pessoa Física) em Python 3, podemos empregar o Negative Lookahead para criar uma expressão regular 
que rejeita padrões específicos.

### Código de Exemplo:

```python
import re
from pprint import pprint

# Expressão regular com Negative Lookahead
regex = re.compile(
    r"^(?!(\d)\1{2}\.\1{3}\.\1{3}-\1{2})(\d{3}\.\d{3}\.\d{3}-\d{2})$",
    flags=re.MULTILINE
)

# Conjunto de CPFs para teste
test_str = (
    "698.547.520-54\n"
    # (Outros CPFs aqui...)
)

# Encontrar todos os CPFs válidos na string de teste
pprint(regex.findall(test_str))
```

### Explicação:

1. `^`: Indica o início da linha.
2. `(?! ...)`: Negative Lookahead, uma construção que nega a ocorrência de determinado padrão.
   - `(\d)`: Captura um dígito (um dos números do CPF).
   - `\1{2}\.\1{3}\.\1{3}-\1{2}`: Especifica o padrão que deve ser evitado (CPF com dígitos repetidos).
3. `(\d{3}\.\d{3}\.\d{3}-\d{2})`: Captura o padrão de um CPF válido.
4. `$`: Indica o final da linha.
5. `flags=re.MULTILINE`: Permite que o caractere `^` e `$` correspondam ao início e ao final de cada linha.

### Teste:

O conjunto de CPFs fornecido em `test_str` é utilizado para testar a expressão regular. A função `findall` retorna 
todos os CPFs válidos encontrados na string.

### Observação:

Este exemplo valida CPFs que não possuem dígitos repetidos em sequência, o que é uma condição adicional à validação padrão. 
Os CPFs inválidos, como "000.000.000-00" ou "111.111.111-11", não são aceitos devido à utilização do Negative Lookahead.
