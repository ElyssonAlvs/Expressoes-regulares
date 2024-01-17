# Validando Números com Expressões Regulares em Python 3

As expressões regulares (regex) em Python são uma poderosa ferramenta para realizar validações em strings de 
forma eficiente. O código apresenta duas funções principais: `is_int` e `is_float`, que utilizam expressões regulares 
para verificar se uma dada string representa um número inteiro ou um número de ponto flutuante, respectivamente.

### **Exemplo de Uso:**

```python
import re

# String contendo exemplos de números válidos e inválidos
string = '''
Válidos
0.0
00.00
... (restante da string)
'''

# Função para validar se uma string é um número inteiro
def is_int(string):
    return bool(re.search(r'^[+-]?\d+$', string))

# Função para validar se uma string é um número de ponto flutuante
def is_float(string):
    return bool(re.search(r'^[+-]?\d+(?:\.\d+)?$', string))

# Loop para entrada do usuário
while True:
    numero = input('Digite um número: ')

    # Verifica se é um número inteiro
    if is_int(numero):
        numero = int(numero)
        print(f'O número {numero} foi convertido para int')
        continue

    # Verifica se é um número de ponto flutuante
    if is_float(numero):
        numero = float(numero)
        print(f'O número {numero} foi convertido para float')
        continue
```

### **Entendendo as Expressões Regulares:**

- `^`: Representa o início da string.
- `[+-]?`: Indica que pode haver um sinal positivo ou negativo opcional no início.
- `\d+`: Corresponde a um ou mais dígitos.
- `(?:\.\d+)?`: Permite a existência opcional de parte decimal após um ponto.
- `$`: Indica o final da string.

### **Exemplos de Números Válidos:**
- 0.0
- +000.000
- -8.5
- 1231345458.54654564
- +1.11123123

### **Exemplos de Números Inválidos:**
- 10..2
- ++1213
- .124546
- 10.
- 5a
- b5

Ao executar o código, o programa solicita ao usuário que digite um número, valida a entrada usando as expressões 
regulares e converte o número para inteiro ou ponto flutuante, informando o resultado ao usuário.