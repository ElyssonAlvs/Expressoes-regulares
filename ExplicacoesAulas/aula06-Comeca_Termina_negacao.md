# Começa com (^), Termina com ($) e Negação em Expressões Regulares em Python 3

```python
# Meta caracteres:
# ^ -> começa com
# $ -> termina com
# [^a-z] -> Negação

import re

# Exemplo de CPF
cpf = '147.852.963-12'

# Verifica se o CPF está formatado corretamente (começa e termina conforme o padrão)
print(re.findall(r'^((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})$', cpf))

# Remove todos os caracteres que não são números, letras ou pontos e hífens
print(re.findall(r'[^0-9a-zA-Z.-]+', cpf))
```

1. **Começa com (^):**
   - A expressão `^((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})$` verifica se a string `cpf` começa e termina conforme o padrão de um CPF. Explicando detalhadamente:
      - `^` indica que a string deve começar com o padrão seguinte.
      - `(?:[0-9]{3}\.){2}` representa dois grupos de três dígitos seguidos por ponto, totalizando seis dígitos e dois pontos.
      - `[0-9]{3}` representa mais três dígitos.
      - `-` é o traço que separa os últimos dois dígitos.
      - `[0-9]{2}` representa os dois últimos dígitos do CPF.
      - `$` indica que a string deve terminar com o padrão anterior.

2. **Negação ([^a-z]):**
   - A expressão `[^0-9a-zA-Z.-]+` remove da string `cpf` todos os caracteres que não são números, letras maiúsculas, letras minúsculas, pontos ou hífens.
      - `[^...]` nega a classe de caracteres, indicando que queremos remover qualquer caractere que não esteja incluído nessa classe.
      - `0-9a-zA-Z.-` inclui todos os dígitos, letras (maiúsculas e minúsculas), pontos e hífens.
      - `+` indica que um ou mais desses caracteres consecutivos devem ser removidos.
