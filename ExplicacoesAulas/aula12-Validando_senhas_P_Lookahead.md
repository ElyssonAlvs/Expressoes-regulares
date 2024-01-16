# Validando Senhas Fortes com Positive Lookahead em Expressões Regulares em Python 3

**Objetivo:**
Validar senhas fortes usando expressões regulares em Python 3, com destaque para o uso de Positive 
Lookahead.

**Código Exemplo:**
```python
import re
senha_forte_regexp = re.compile(
    r'^'
    r'(?=.*[a-z])'
    r'(?=.*[A-Z])'
    r'(?=.*[0-9])'
    r'(?=.*[ -\/:-@[-`{-~])'
    r'.{12,}'
    r'$',
    flags=re.M
)
```

**Explicação Detalhada:**
1. **(?=.*[a-z]):** Deve conter pelo menos uma letra minúscula.
2. **(?=.*[A-Z]):** Deve conter pelo menos uma letra maiúscula.
3. **(?=.*[0-9]):** Deve conter pelo menos um número.
4. **(?=.*[ -\/:-@[-`{-~]):** Deve conter pelo menos um caractere especial (definido no conjunto de caracteres Unicode).
5. **.{12,}:** Deve ter pelo menos 12 caracteres de comprimento.
6. **$:** Indica que a validação deve ocorrer até o final da string.
7. **flags=re.M:** Ativa o modo de várias linhas, permitindo que ^ e $ correspondam ao início e ao fim de cada linha.

**Exemplos:**
- **VÁLIDAS:** Senhas que atendem a todos os critérios.
- **SEM MINÚSCULAS:** Senhas sem letras minúsculas.
- **SEM MINÚSCULAS E NÚMEROS:** Senhas sem letras minúsculas e números.
- **SEM NÚMEROS, CARACTERES E MINÚSCULAS:** Senhas sem números, caracteres especiais e letras minúsculas.
- **QUANTIDADE INVÁLIDA (6):** Senhas com comprimento inferior a 12 caracteres.

**Utilização Prática:**
```python
string = '''
VÁLIDAS
... (senhas válidas)
'''

print(senha_forte_regexp.findall(string))
```

**Observação:**
O Positive Lookahead (?=) permite validar condições sem consumir caracteres na string, facilitando a construção de 
expressões regulares complexas para validação de padrões específicos.
