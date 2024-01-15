# Expressões Regulares em Python 3: Lookahead e Lookbehind

As expressões regulares (regex) são poderosas ferramentas para buscar e manipular padrões de texto em Python. Dois conceitos
avançados dentro das regex são Lookahead e Lookbehind, que permitem definir condições para correspondências que não são 
diretamente parte da correspondência principal.

1. **Positive Lookahead:**

   - Exemplo: `(?=active)`

   - Descrição: Busca por padrões que são seguidos por "active". No exemplo fornecido, busca por endereços IP precedidos 
   pela palavra "active".

2. **Negative Lookahead:**

   - Exemplo: `(?!active)`

   - Descrição: Busca por padrões que não são seguidos por "active". No exemplo, encontra endereços IP não seguidos pela palavra "active".

3. **Positive Lookbehind:**

   - Exemplo: `(?<=ONLINE)`

   - Descrição: Busca por padrões que são precedidos por "ONLINE". No exemplo, encontra palavras que estão após a palavra 
   "ONLINE" (no caso, endereços IP).

4. **Negative Lookbehind:**

   - Exemplo: `(?<!ONLINE)`

   - Descrição: Busca por padrões que não são precedidos por "ONLINE". No exemplo, encontra palavras que não estão após 
   a palavra "ONLINE".

**Exemplo de Uso no Código Fornecido:**

```python
import re
from pprint import pprint

texto = '''
ONLINE  192.168.0.1 GHIJK active
OFFLINE  192.168.0.2 GHIJK inactive
OFFLINE  192.168.0.3 GHIJK active
ONLINE  192.168.0.4 GHIJK active
ONLINE  192.168.0.5 GHIJK inactive
OFFLINE  192.168.0.6 GHIJK active
'''

# Positive lookahead
pprint(re.findall(r'\w+\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+(?=active)', texto))

# Negative lookahead
pprint(re.findall(r'\w+\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+(?!active)', texto))

# Positive lookbehind
pprint(re.findall(r'\w+(?<=ONLINE)\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+\w+', texto))

# Negative lookbehind
pprint(re.findall(r'\w+(?<!ONLINE)\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+\w+', texto))
```

Estas construções avançadas em regex são poderosas para filtrar padrões complexos em textos, oferecendo flexibilidade e 
controle nas correspondências.