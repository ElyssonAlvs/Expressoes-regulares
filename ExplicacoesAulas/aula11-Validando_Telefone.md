# Resumo Didático: Desafio de Validação de Telefone com Expressões Regulares em Python 3

**Introdução:**
A validação de telefones é um desafio comum na programação, e expressões regulares (regex) são uma ferramenta 
poderosa para lidar com esse tipo de tarefa.

**Código de Exemplo:**
```python
import re

# Expressão Regular
regexp = re.compile(r'^(?:\(\d{2}\)\s)(?:9\s)(?:\d{4}-\d{4})$', flags=re.M)

# Texto de Exemplo
texto = '''
(21) 9 8852-5214
(11)9955-1231
(11)            9955-1231
(35) 9 9975-4521
(31) 3851-2587
9 8571-5213
1234-5647
'''

# Encontrar e Imprimir Telefones Válidos
for telefone in regexp.findall(texto):
    print(telefone)
```

**Explicação:**

1. **Expressão Regular:**
   - `^(?:\(\d{2}\)\s)`: Inicia a expressão exigindo um código de área entre parênteses e um espaço.
   - `(?:9\s)`: Garante que o número inicie com o dígito 9 e um espaço.
   - `(?:\d{4}-\d{4})$`: Define o formato do restante do número, composto por quatro dígitos, um hífen, e mais quatro dígitos.
   - `flags=re.M`: Permite que a expressão regular seja aplicada a cada linha do texto.

2. **Texto de Exemplo:**
   - Contém uma lista de números de telefone, alguns válidos e outros inválidos.

3. **Loop de Validação:**
   - Utiliza `findall` para encontrar todas as correspondências da expressão regular no texto.
   - Imprime os telefones válidos.

**Resultado:**
O código produzirá a saída apenas com os números de telefone que correspondem à expressão regular, validando efetivamente 
os números específicos desejados.

**Conclusão:**
As expressões regulares são ferramentas poderosas para validar e manipular padrões em textos, tornando-as ideais para 
desafios como a validação de números de telefone.